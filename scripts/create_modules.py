# scripts/create_modules.py
"""
Creates new enablement modules from source documentation.
Used for initial module generation, not updates.
"""

import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv
import argparse

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def load_source_docs(source_files):
    """Load specified source documentation files."""
    docs_content = "# Source Documentation\n\n"
    
    for filepath in source_files:
        if not os.path.exists(filepath):
            print(f"⚠ Warning: {filepath} not found, skipping")
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                docs_content += f"## {filepath}\n\n{content}\n\n---\n\n"
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
    
    return docs_content

def create_module(module_spec, source_docs, output_dir='enablement-modules'):
    """
    Create a single enablement module based on specifications.
    
    Args:
        module_spec: Dict with 'filename', 'title', and 'description'
        source_docs: String containing all source documentation
        output_dir: Directory to save the module
    """
    
    prompt = f"""You are creating technical enablement content for live instructor-led training sessions.

## Module Specifications

**Filename**: {module_spec['filename']}
**Module Title**: {module_spec['title']}
**Coverage**: {module_spec['description']}

## Your Task

Create a comprehensive enablement module that will be:
1. Used as reference material for instructors delivering live training
2. Eventually converted into PowerPoint slides with talk tracks
3. Delivered in instructor-led sessions

## Module Structure Requirements

1. **Learning Objectives** (3-5 clear, measurable objectives)
2. **Overview** (brief introduction to the topic)
3. **Core Content** (main instructional content, organized in logical sections)
   - Use clear headings and subheadings
   - Include practical examples
   - Add "Instructor Note:" callouts where helpful for live delivery
   - Include discussion prompts or questions to engage learners
4. **Hands-On Activity or Demo** (if applicable - something the instructor can demonstrate)
5. **Key Takeaways** (3-5 bullet summary)
6. **Additional Resources** (links or references for deeper learning)

## Style Guidelines

- Write in a conversational but professional tone (this will be spoken aloud)
- Use second person ("you") when addressing learners
- Include concrete examples and scenarios
- Anticipate common questions learners might ask
- Keep technical accuracy while maintaining accessibility
- Use markdown formatting for clarity

Create the complete module content now."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8000,
            system=[
                {
                    "type": "text",
                    "text": "You are an expert instructional designer specializing in technical enablement for enterprise software."
                },
                {
                    "type": "text",
                    "text": source_docs,
                    "cache_control": {"type": "ephemeral"}
                }
            ],
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # Extract content
        content = ""
        for block in response.content:
            if block.type == "text":
                content += block.text
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Save module
        output_path = os.path.join(output_dir, module_spec['filename'])
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"✗ Error creating {module_spec['filename']}: {e}")
        return None

def create_modules_from_specs(specs_file, source_files):
    """Create multiple modules from a specifications file."""
    
    # Load module specifications
    with open(specs_file, 'r') as f:
        specs = json.load(f)
    
    # Load source documentation (with caching)
    print("Loading source documentation...")
    source_docs = load_source_docs(source_files)
    print(f"✓ Loaded {len(source_docs)} characters from {len(source_files)} source files\n")
    
    # Create each module
    created_modules = []
    for i, module_spec in enumerate(specs['modules'], 1):
        print(f"Creating module {i}/{len(specs['modules'])}: {module_spec['title']}...")
        output_path = create_module(module_spec, source_docs)
        if output_path:
            created_modules.append(output_path)
        print()
    
    return created_modules

def interactive_mode(source_files):
    """Interactive mode - prompt user for module specifications."""
    
    print("\n=== Interactive Module Creation ===\n")
    print("Enter module specifications. Type 'done' when finished.\n")
    
    modules = []
    module_num = 1
    
    while True:
        print(f"\n--- Module {module_num} ---")
        
        title = input("Module title (or 'done' to finish): ").strip()
        if title.lower() == 'done':
            break
        
        description = input("What should this module cover? ").strip()
        
        # Generate filename from title
        filename = f"module-{module_num}-{title.lower().replace(' ', '-')}.md"
        
        modules.append({
            "filename": filename,
            "title": title,
            "description": description
        })
        
        module_num += 1
    
    if not modules:
        print("\nNo modules specified. Exiting.")
        return
    
    # Save specs to temp file
    specs = {"modules": modules}
    with open('module-specs-temp.json', 'w') as f:
        json.dump(specs, indent=2, fp=f)
    
    print(f"\n✓ Will create {len(modules)} modules")
    proceed = input("Proceed with creation? (y/n): ").strip().lower()
    
    if proceed == 'y':
        created = create_modules_from_specs('module-specs-temp.json', source_files)
        print(f"\n✓ Successfully created {len(created)} modules!")
        
        # Clean up temp file
        os.remove('module-specs-temp.json')
    else:
        print("Cancelled.")

def main():
    parser = argparse.ArgumentParser(
        description='Create new enablement modules from source documentation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  
  # Interactive mode - prompts you for module specs
  python scripts/create_modules.py --source source-docs/plugins.md --interactive
  
  # From a specifications file
  python scripts/create_modules.py --source source-docs/plugins.md --specs module-specs.json
        """
    )
    
    parser.add_argument('--source', nargs='+', required=True,
                       help='Source documentation file(s) to use as reference')
    parser.add_argument('--specs', 
                       help='JSON file with module specifications')
    parser.add_argument('--interactive', action='store_true',
                       help='Interactive mode - prompts for module specs')
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode(args.source)
    elif args.specs:
        created = create_modules_from_specs(args.specs, args.source)
        print(f"\n✓ Successfully created {len(created)} modules!")
    else:
        print("Error: Must specify either --interactive or --specs")
        parser.print_help()
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())