#!/usr/bin/env python3
"""
Analyze the impact of source doc changes on enablement modules.
Uses Claude to determine which modules need updates based on changed files.
"""

import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Resolve project root (parent of scripts/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def read_file(path: str) -> str:
    """Read file content, return empty string if not found."""
    full_path = PROJECT_ROOT / path
    try:
        return full_path.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError):
        return ""


def get_enablement_modules() -> list[str]:
    """List all enablement module files."""
    modules_dir = PROJECT_ROOT / "enablement-modules"
    if not modules_dir.exists():
        return []
    return [
        str(f.relative_to(PROJECT_ROOT))
        for f in modules_dir.glob("*.md")
    ]


def analyze_impact(changed_files: list[str], module_paths: list[str]) -> dict:
    """Use Claude to analyze which modules are affected by doc changes."""
    changed_content = {}
    for f in changed_files:
        content = read_file(f)
        if content:
            changed_content[f] = content

    module_content = {}
    for m in module_paths:
        content = read_file(m)
        if content:
            module_content[m] = content

    if not changed_content:
        return {"changed_files": changed_files, "affected_modules": [], "error": "No changed file content found"}

    client = Anthropic()
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set. Add it to .env or set the environment variable.")

    prompt = f"""Analyze the impact of these source documentation changes on the enablement modules.

## Changed Source Files
{json.dumps(changed_content, indent=2)}

## Existing Enablement Modules
{json.dumps(module_content, indent=2)}

## Your Task
For each changed source file, determine which enablement modules (if any) need to be updated based on the content changes. Consider:
- Overlapping topics and concepts
- Outdated information that modules may reference
- New information that should be incorporated
- Ripple effects (e.g., a product overview change may affect multiple modules)

Respond with a JSON object only, no other text. Use this exact structure:
{{
  "changed_files": ["list", "of", "changed", "paths"],
  "affected_modules": [
    {{
      "module": "path/to/module.md",
      "reason": "Brief explanation of why this module needs updating",
      "priority": "high" | "medium" | "low"
    }}
  ]
}}"""

    response = client.messages.create(
        model=os.environ.get("ANTHROPIC_MODEL", "claude-4-6-opus-latest"),
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text
    # Extract JSON (handle potential markdown code block)
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()

    return json.loads(text)


def mock_impact(changed_files: list[str], module_paths: list[str]) -> dict:
    """Return mock impact analysis without calling the API (for testing)."""
    return {
        "changed_files": changed_files,
        "affected_modules": [
            {"module": m, "reason": "Placeholder - run without --mock to use Claude analysis", "priority": "medium"}
            for m in module_paths
        ],
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze impact of source doc changes on enablement modules")
    parser.add_argument("--changed-files", required=True, help="Space-separated list of changed file paths")
    parser.add_argument("--output", required=True, help="Output JSON file path")
    parser.add_argument("--mock", action="store_true", help="Skip API call; output mock analysis for testing")
    args = parser.parse_args()

    changed_files = [f.strip() for f in args.changed_files.split() if f.strip()]
    module_paths = get_enablement_modules()

    print(f"Analyzing impact of {len(changed_files)} changed file(s) on {len(module_paths)} module(s)...")
    result = mock_impact(changed_files, module_paths) if args.mock else analyze_impact(changed_files, module_paths)

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = PROJECT_ROOT / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"Impact analysis written to {output_path}")
    affected = result.get("affected_modules", [])
    print(f"Modules requiring updates: {len(affected)}")
    for m in affected:
        print(f"  - {m.get('module', '?')} ({m.get('priority', '?')}): {m.get('reason', '')[:60]}...")


if __name__ == "__main__":
    main()
