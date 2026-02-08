# scripts/generate_enablement.py
"""
Generates or updates enablement modules using Claude's Batch API.
Uses prompt caching for efficiency with large source documents.
"""

import os
import json
import time
from anthropic import Anthropic
from dotenv import load_dotenv
import argparse

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def load_source_docs(source_dir='source-docs'):
    """Load all source documentation to use as cached context."""
    docs_content = "# Source Documentation Library\n\n"
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        docs_content += f"## {filepath}\n\n{content}\n\n---\n\n"
                except Exception as e:
                    print(f"Error loading {filepath}: {e}")
    
    return docs_content

def create_batch_requests(impact_analysis, source_docs_cache):
    """Create batch API requests for updating modules."""
    
    requests = []
    
    for i, module_info in enumerate(impact_analysis.get('affected_modules', [])):
        module_path = module_info['module_path']
        changes_needed = module_info['changes_needed']
        
        # Load existing module content if it exists
        existing_content = ""
        if os.path.exists(module_path):
            with open(module_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
        
        prompt = f"""You are creating technical enablement content for Splunk products.

Your task: Update the following enablement module based on recent documentation changes.

## Current Module Content:
{existing_content if existing_content else "This is a new module."}

## Required Changes:
{json.dumps(changes_needed, indent=2)}

## Impact Level: {module_info['impact_level']}

## Guidelines:
- Maintain clear, instructional tone appropriate for technical enablement
- Include practical examples where relevant
- Structure content with clear learning objectives
- Use markdown formatting
- Ensure accuracy based on source documentation

Please provide the complete updated module content."""

        # Create batch request with prompt caching
        request = {
            "custom_id": f"module-update-{i}",
            "params": {
                "model": "claude-4-5-sonnet-latest",
                "max_tokens": 8000,
                "system": [
                    {
                        "type": "text",
                        "text": "You are an expert technical enablement content creator specializing in enterprise software training."
                    },
                    {
                        "type": "text",
                        "text": source_docs_cache,
                        "cache_control": {"type": "ephemeral"}
                    }
                ],
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        }
        
        requests.append({
            "request": request,
            "module_path": module_path
        })
    
    return requests

def submit_batch(requests):
    """Submit batch processing job to Claude API."""
    
    # Create the batch file format
    batch_requests = [r["request"] for r in requests]
    
    try:
        # Create message batch
        message_batch = client.messages.batches.create(
            requests=batch_requests
        )
        
        print(f"✓ Batch submitted: {message_batch.id}")
        print(f"  Status: {message_batch.processing_status}")
        
        return message_batch.id, requests
        
    except Exception as e:
        print(f"✗ Error submitting batch: {e}")
        return None, None

def poll_batch_status(batch_id, timeout=600):
    """Poll batch status until complete or timeout."""
    
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            batch = client.messages.batches.retrieve(batch_id)
            status = batch.processing_status
            
            print(f"  Status: {status} (elapsed: {int(time.time() - start_time)}s)")
            
            if status == "ended":
                return batch
            
            time.sleep(10)  # Poll every 10 seconds
            
        except Exception as e:
            print(f"Error checking batch status: {e}")
            time.sleep(10)
    
    print("✗ Batch processing timeout")
    return None

def process_batch_results(batch_id, request_mapping):
    """Retrieve and save batch results."""
    
    try:
        # Get all results
        results = client.messages.batches.results(batch_id)
        
        updated_files = []
        
        for result in results:
            custom_id = result.custom_id
            
            # Find the corresponding module path
            module_path = None
            for req in request_mapping:
                if req["request"]["custom_id"] == custom_id:
                    module_path = req["module_path"]
                    break
            
            if not module_path:
                print(f"⚠ Could not find module path for {custom_id}")
                continue
            
            # Extract the generated content
            if result.result.type == "succeeded":
                message = result.result.message
                content_text = ""
                
                for block in message.content:
                    if block.type == "text":
                        content_text += block.text
                
                # Ensure directory exists
                os.makedirs(os.path.dirname(module_path), exist_ok=True)
                
                # Save updated module
                with open(module_path, 'w', encoding='utf-8') as f:
                    f.write(content_text)
                
                updated_files.append(module_path)
                print(f"✓ Updated: {module_path}")
            else:
                print(f"✗ Failed to generate {module_path}: {result.result.type}")
        
        return updated_files
        
    except Exception as e:
        print(f"✗ Error processing results: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description='Generate enablement content updates')
    parser.add_argument('--impact-file', default='impact-analysis.json',
                       help='Path to impact analysis JSON file')
    
    args = parser.parse_args()
    
    # Load impact analysis
    if not os.path.exists(args.impact_file):
        print(f"✗ Impact analysis file not found: {args.impact_file}")
        return 1
    
    with open(args.impact_file, 'r') as f:
        impact_analysis = json.load(f)
    
    print("Loading source documentation for caching...")
    source_docs = load_source_docs()
    print(f"✓ Loaded {len(source_docs)} characters of source docs")
    
    print("\nCreating batch requests...")
    request_mapping = create_batch_requests(impact_analysis, source_docs)
    
    if not request_mapping:
        print("No modules to update")
        return 0
    
    print(f"✓ Created {len(request_mapping)} update requests")
    
    print("\nSubmitting batch to Claude API...")
    batch_id, mapping = submit_batch(request_mapping)
    
    if not batch_id:
        return 1
    
    print("\nWaiting for batch processing to complete...")
    batch = poll_batch_status(batch_id)
    
    if not batch:
        return 1
    
    print("\n✓ Batch processing complete!")
    print(f"  Requests: {batch.request_counts.processing}")
    
    print("\nRetrieving and saving results...")
    updated_files = process_batch_results(batch_id, mapping)
    
    print(f"\n✓ Successfully updated {len(updated_files)} enablement modules")
    
    return 0

if __name__ == '__main__':
    exit(main())