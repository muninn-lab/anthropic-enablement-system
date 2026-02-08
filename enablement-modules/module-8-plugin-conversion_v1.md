> v1 | **Last updated: 2/8/2026**

> Module Title: Converting Configurations to Plugins

> Description: Cover the step-by-step migration process, troubleshooting common issues, and best practices for plugin conversions. Include a plugin conversion walkthrough as demo.


# Convert existing configurations to plugins

If you already have skills or hooks in your `.claude/` directory, you can convert them into a plugin for easier sharing and distribution.

## Workflow
1. Create the plugin structure
2. Copy your existing files
3. Migrate hooks
4. Test your migrated plugin

## What changes when migrating

| Standalone (`.claude/`)       | Plugin                           |
| :---------------------------- | :------------------------------- |
| Only available in one project | Can be shared via marketplaces   |
| Files in `.claude/commands/`  | Files in `plugin-name/commands/` |
| Hooks in `settings.json`      | Hooks in `hooks/hooks.json`      |
| Must manually copy to share   | Install with `/plugin install`   |

<Note>
  After migrating, you can remove the original files from `.claude/` to avoid duplicates. The plugin version will take precedence when loaded.
</Note>

# Demo: convert configurations to a plugin