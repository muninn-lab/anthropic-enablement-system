Module Title: Installing and Managing Plugins

Description: Cover the step-by-step installation process, managing installed plugins, troubleshooting common issues, and best practices for plugin management. Include a plugin installation walkthrough as demo.

# Install plugins

Once you've added marketplaces, you can install plugins directly (installs to user scope by default):

```shell  theme={null}
/plugin install plugin-name@marketplace-name
```

To choose a different installation scope, use the interactive UI: run `/plugin`, go to the **Discover** tab, and press **Enter** on a plugin. You'll see options for:

* **User scope** (default): install for yourself across all projects
* **Project scope**: install for all collaborators on this repository (adds to `.claude/settings.json`)
* **Local scope**: install for yourself in this repository only (not shared with collaborators)

You may also see plugins with **managed** scope—these are installed by administrators via managed settings and cannot be modified.

Run `/plugin` and go to the **Installed** tab to see your plugins grouped by scope.

<Warning>
  Make sure you trust a plugin before installing it. Anthropic does not control what MCP servers, files, or other software are included in plugins and cannot verify that they work as intended. Check each plugin's homepage for more information.
</Warning>

# Manage installed plugins

Run `/plugin` and go to the **Installed** tab to view, enable, disable, or uninstall your plugins. Type to filter the list by plugin name or description.

You can also manage plugins with direct commands.

Disable a plugin without uninstalling:

```shell  theme={null}
/plugin disable plugin-name@marketplace-name
```

Re-enable a disabled plugin:

```shell  theme={null}
/plugin enable plugin-name@marketplace-name
```

Completely remove a plugin:

```shell  theme={null}
/plugin uninstall plugin-name@marketplace-name
```

The `--scope` option lets you target a specific scope with CLI commands:

```shell  theme={null}
claude plugin install formatter@your-org --scope project
claude plugin uninstall formatter@your-org --scope project
```

# Demo: install a plugin