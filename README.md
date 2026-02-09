# README.md
# Anthropic Enablement System - 'Plugins & Marketplaces'

Automated technical enablement content maintenance using Claude AI.

## How It Works

1. **Source of Truth**: Product docs, PRDs, runbooks, and other artifacts live in `source-docs/`
2. **Change Detection**: GitHub Actions monitors changes to source docs
3. **Impact Analysis**: Claude analyzes which enablement modules need updates
4. **Batch Generation**: Updated modules are generated via Claude's Batch API `enablement-materials/`
5. **Human Review**: Changes are submitted as PRs for SME validation
6. **Ready to Teachs**: Training ready content made available `trainer-resources/`

## Setup

1. Clone this repository
2. Copy `.env.example` to `.env` and add your Anthropic API key
3. Add your API key as a GitHub secret: `ANTHROPIC_API_KEY`
4. Add source documentation to `source-docs/`
5. Initial enablement modules go in `enablement-modules/`
6. Final educator materials go in `trainer-resources/`

## Local Testing
```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Run impact analysis
python scripts/analyze_impact.py \
  --changed-files source-docs/product-overview.md \
  --output impact-analysis.json

# Generate updates
python scripts/generate_enablement.py --impact-file impact-analysis.json
```

## Architecture

- **Prompt Caching**: Source docs are cached to reduce API costs by ~90%
- **Batch API**: Module updates processed asynchronously at 50% cost savings
- **Extended Thinking**: Impact analysis uses deep reasoning to identify ripple effects
