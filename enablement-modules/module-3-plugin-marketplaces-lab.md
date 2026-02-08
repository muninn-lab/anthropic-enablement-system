Module Title: Lab: Adding the Demo Marketplace

Description: Add the demo marketplace and browse the plugins.

# Introduction

This lab walks you through adding the Anthropic demo marketplace to browse example plugins that show what's possible with the plugin system. Unlike the official marketplace, you need to add this one manually.

## Steps

<Steps>
  <Step title="Add the marketplace">
    From within Claude Code, run the `plugin marketplace add` command for the `anthropics/claude-code` marketplace:

    ```shell  theme={null}
    /plugin marketplace add anthropics/claude-code
    ```

    This downloads the marketplace catalog and makes its plugins available to you.
  </Step>

  <Step title="Browse available plugins">
    Run `/plugin` to open the plugin manager. This opens a tabbed interface with four tabs you can cycle through using **Tab** (or **Shift+Tab** to go backward):

    * **Discover**: browse available plugins from all your marketplaces
    * **Installed**: view and manage your installed plugins
    * **Marketplaces**: add, remove, or update your added marketplaces
    * **Errors**: view any plugin loading errors

    Go to the **Discover** tab to see plugins from the marketplace you just added.
  </Step>

  <Step title="Install a plugin">
    Select a plugin to view its details, then choose an installation scope:

    * **User scope**: install for yourself across all projects
    * **Project scope**: install for all collaborators on this repository
    * **Local scope**: install for yourself in this repository only

    For example, select **commit-commands** (a plugin that adds git workflow commands) and install it to your user scope.

    You can also install directly from the command line:

    ```shell  theme={null}
    /plugin install commit-commands@anthropics-claude-code
    ```

    See [Configuration scopes](/en/settings#configuration-scopes) to learn more about scopes.
  </Step>

  <Step title="Use your new plugin">
    After installing, the plugin's commands are immediately available. Plugin commands are namespaced by the plugin name, so **commit-commands** provides commands like `/commit-commands:commit`.

    Try it out by making a change to a file and running:

    ```shell  theme={null}
    /commit-commands:commit
    ```

    This stages your changes, generates a commit message, and creates the commit.

    Each plugin works differently. Check the plugin's description in the **Discover** tab or its homepage to learn what commands and capabilities it provides.
  </Step>
</Steps>