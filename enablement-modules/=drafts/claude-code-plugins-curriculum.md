# Claude Code Plugins Training Curriculum

## Course Overview

**Course Title:** Mastering Claude Code Plugins: From Discovery to Distribution

**Target Audience:** Technical developers (Anthropic employees, partners, and customers)

**Duration:** 6-8 hours (self-paced)

**Prerequisites:** 
- Claude Code installed and authenticated
- Claude Code version 1.0.33 or later
- Basic command-line experience
- Familiarity with JSON and directory structures

**Course Description:**
This comprehensive training enables developers to discover, install, create, and distribute Claude Code plugins. Through a blend of conceptual learning and hands-on labs, participants will master the plugin ecosystem—from understanding when to use plugins versus standalone configurations to building sophisticated custom plugins with skills, agents, hooks, and MCP servers.

---

## Module 1: What Plugins Are and How They Work

**Duration:** 45 minutes

**Learning Objectives:**
By the end of this module, learners will be able to:
- Define what Claude Code plugins are and explain their purpose in the extension ecosystem
- Compare plugins versus standalone configurations and determine appropriate use cases for each
- Explain how plugin namespacing prevents conflicts between extensions
- Identify the types of functionality plugins can add (skills, agents, hooks, MCP servers)

**Key Concepts:**
- Plugin fundamentals and architecture
- Standalone `.claude/` directory vs plugin packages
- Plugin namespacing conventions (`/plugin-name:command`)
- When to use plugins (sharing, versioning, reusability)
- When to use standalone configurations (personal workflows, experiments)

**Content Outline:**
1. Introduction to the plugin system
2. Plugin capabilities overview (skills, agents, hooks, MCP servers)
3. Decision framework: plugins vs standalone
4. Naming conventions and namespacing
5. Real-world plugin examples

**Knowledge Check Questions:**

1. **Which scenario is BEST suited for creating a plugin rather than using standalone configuration?**
   - A) You're experimenting with a new skill for personal use
   - B) You need to share custom functionality with your entire team
   - C) You want a short skill name like `/hello`
   - D) You're customizing Claude Code for a single project
   
   **Answer:** B
   **Explanation:** Plugins are ideal for sharing functionality across teams and projects. Standalone configurations are better for personal or project-specific customizations.

2. **What is the primary purpose of plugin namespacing?**
   - A) To make commands longer and more descriptive
   - B) To prevent naming conflicts between different plugins
   - C) To organize files within the plugin directory
   - D) To distinguish between user and system commands
   
   **Answer:** B
   **Explanation:** Namespacing ensures that skills from different plugins don't conflict even if they have similar names (e.g., `/plugin-a:hello` vs `/plugin-b:hello`).

3. **A developer wants to create a custom code review skill that they'll use across multiple projects and potentially share with colleagues in the future. They also want short skill names. What approach should they take?**
   - A) Start with a plugin from the beginning
   - B) Create standalone configuration in `.claude/` first, then convert to a plugin later
   - C) Use both approaches simultaneously
   - D) Wait until they're ready to share before creating anything
   
   **Answer:** B
   **Explanation:** The best practice is to start with standalone configuration for quick iteration and short names, then convert to a plugin when ready to share.

4. **Which of the following can plugins include? (Select all that apply)**
   - A) Custom skills
   - B) Agent definitions
   - C) Event hooks
   - D) MCP servers
   
   **Answer:** All (A, B, C, D)
   **Explanation:** Plugins are comprehensive packages that can include skills, agents, hooks, MCP servers, and even LSP servers.

---

## Module 2: Plugin Marketplaces

**Duration:** 30 minutes

**Learning Objectives:**
By the end of this module, learners will be able to:
- Explain the purpose of plugin marketplaces in the Claude Code ecosystem
- Distinguish between official and community/demo marketplaces
- Navigate the plugin discovery interface to find relevant plugins
- Evaluate plugin security and trustworthiness before installation

**Key Concepts:**
- Marketplace architecture and catalog system
- Official vs demo marketplaces
- Plugin discovery workflow
- Security considerations and trust model
- The four-tab plugin manager interface

**Content Outline:**
1. What are plugin marketplaces?
2. Marketplace types and sources
3. The plugin manager interface:
   - Discover tab
   - Installed tab
   - Marketplaces tab
   - Errors tab
4. Security and trust considerations
5. Evaluating plugins before installation

**Knowledge Check Questions:**

1. **What command opens the plugin manager interface in Claude Code?**
   - A) `/plugins`
   - B) `/plugin`
   - C) `/marketplace`
   - D) `/discover`
   
   **Answer:** B
   **Explanation:** The `/plugin` command opens the tabbed plugin manager interface with Discover, Installed, Marketplaces, and Errors tabs.

2. **Which tab in the plugin manager shows plugins available for installation?**
   - A) Installed
   - B) Marketplaces
   - C) Discover
   - D) Browse
   
   **Answer:** C
   **Explanation:** The Discover tab displays all available plugins from your added marketplaces.

3. **Before installing a plugin, what should developers verify?**
   - A) The plugin's source code
   - B) The plugin's homepage for information about its functionality
   - C) The number of downloads
   - D) The plugin's file size
   
   **Answer:** B
   **Explanation:** The documentation emphasizes checking the plugin's homepage for information, as Anthropic doesn't verify plugin functionality or control their contents.

---

## Module 3: Lab - Adding the Demo Marketplace

**Duration:** 20 minutes

**Learning Objectives:**
By the end of this lab, learners will be able to:
- Add a marketplace to Claude Code using the CLI
- Navigate the four-tab plugin manager interface
- Browse available plugins in a marketplace
- Understand the difference between official and demo marketplaces

**Lab Steps:**
1. Add the demo marketplace using `/plugin marketplace add anthropics/claude-code`
2. Open the plugin manager with `/plugin`
3. Navigate between tabs using Tab and Shift+Tab
4. Explore available plugins in the Discover tab
5. View plugin details and installation options

**Expected Outcomes:**
- Successfully added marketplace appears in Marketplaces tab
- Can browse and view details of demo plugins
- Understands the plugin manager navigation

**Knowledge Check Questions:**

1. **What command adds the Anthropic demo marketplace?**
   - A) `/plugin add anthropics/claude-code`
   - B) `/marketplace add anthropics/claude-code`
   - C) `/plugin marketplace add anthropics/claude-code`
   - D) `/plugin install marketplace anthropics/claude-code`
   
   **Answer:** C
   **Explanation:** The full command path is `/plugin marketplace add` followed by the marketplace identifier.

2. **After adding a marketplace, where do its plugins appear?**
   - A) Immediately in the Installed tab
   - B) In the Discover tab
   - C) In the Marketplaces tab only
   - D) In a separate marketplace window
   
   **Answer:** B
   **Explanation:** Once a marketplace is added, its plugins become available in the Discover tab for browsing and installation.

3. **How do you navigate backward through the plugin manager tabs?**
   - A) Press Escape
   - B) Press Shift+Tab
   - C) Press Backspace
   - D) Press Ctrl+Left Arrow
   
   **Answer:** B
   **Explanation:** Use Tab to move forward through tabs and Shift+Tab to move backward.

---

## Module 4: Installing and Managing Plugins

**Duration:** 45 minutes

**Learning Objectives:**
By the end of this module, learners will be able to:
- Install plugins using both CLI commands and the interactive UI
- Distinguish between user, project, and local installation scopes
- Enable, disable, and uninstall plugins appropriately
- Troubleshoot common installation issues
- Understand managed scope plugins in enterprise settings

**Key Concepts:**
- Installation scopes and their implications
- Plugin lifecycle management
- CLI vs UI installation workflows
- Namespaced plugin commands
- Managed plugins (administrator-controlled)

**Content Outline:**
1. Installation methods (CLI and UI)
2. Understanding installation scopes:
   - User scope (personal, all projects)
   - Project scope (team-shared via `.claude/settings.json`)
   - Local scope (personal, single repository)
   - Managed scope (administrator-controlled)
3. Plugin states: enabled vs disabled
4. Uninstalling plugins
5. Using the `--scope` flag in CLI commands
6. Common troubleshooting scenarios

**Knowledge Check Questions:**

1. **What is the default installation scope when using the command `/plugin install plugin-name@marketplace-name`?**
   - A) Project scope
   - B) Local scope
   - C) User scope
   - D) Global scope
   
   **Answer:** C
   **Explanation:** CLI installation defaults to user scope, which installs the plugin for the user across all projects.

2. **Which installation scope adds the plugin configuration to `.claude/settings.json` for team sharing?**
   - A) User scope
   - B) Project scope
   - C) Local scope
   - D) Shared scope
   
   **Answer:** B
   **Explanation:** Project scope installs plugins for all collaborators on the repository by adding configuration to the project's `.claude/settings.json`.

3. **A developer wants to test a plugin in one repository without affecting their other projects or sharing it with teammates. Which scope should they use?**
   - A) User scope
   - B) Project scope
   - C) Local scope
   - D) Test scope
   
   **Answer:** C
   **Explanation:** Local scope installs the plugin for the user in only this repository, perfect for testing without broader impact.

4. **What does disabling a plugin do?**
   - A) Permanently removes the plugin
   - B) Temporarily prevents the plugin from loading without uninstalling it
   - C) Hides the plugin from the Installed tab
   - D) Revokes the plugin's marketplace access
   
   **Answer:** B
   **Explanation:** Disabling temporarily stops a plugin from loading while keeping it installed, allowing easy re-enabling later.

---

## Module 5: Lab - Installing a Plugin

**Duration:** 20 minutes

**Learning Objectives:**
By the end of this lab, learners will be able to:
- Install a plugin from the demo marketplace
- Use namespaced plugin commands
- Verify plugin installation and functionality
- Switch between different installation scopes

**Lab Steps:**
1. Install the commit-commands plugin using the UI (user scope)
2. Verify installation in the Installed tab
3. Test the plugin with `/commit-commands:commit`
4. Explore the plugin's available commands with `/help`
5. (Optional) Install the same plugin with different scopes to see the difference

**Expected Outcomes:**
- Plugin successfully installed and visible in `/plugin` Installed tab
- Can execute namespaced plugin commands
- Understands how to discover plugin capabilities

**Knowledge Check Questions:**

1. **After installing the commit-commands plugin, what is the correct command to create a commit?**
   - A) `/commit`
   - B) `/commit-commands:commit`
   - C) `/plugin:commit-commands`
   - D) `/commit-commands/commit`
   
   **Answer:** B
   **Explanation:** Plugin commands are namespaced with the format `/plugin-name:command-name`.

2. **Where can you find a list of all commands provided by an installed plugin?**
   - A) In the Discover tab
   - B) By running `/plugin info plugin-name`
   - C) In the plugin's description in the Discover tab or by running `/help`
   - D) In the Errors tab
   
   **Answer:** C
   **Explanation:** Plugin commands and capabilities are shown in the plugin description and are listed when you run `/help`.

3. **What does it mean when a plugin shows "managed" scope in the Installed tab?**
   - A) The user installed it but can manage its settings
   - B) It was installed by an administrator and cannot be modified by the user
   - C) It requires manual updates
   - D) It needs admin approval to use
   
   **Answer:** B
   **Explanation:** Managed scope indicates administrator-installed plugins that users cannot enable, disable, or uninstall.

---

## Module 6: Creating Plugins

**Duration:** 60 minutes

**Learning Objectives:**
By the end of this module, learners will be able to:
- Design an appropriate plugin directory structure
- Create a valid plugin manifest file
- Add skills, agents, hooks, and MCP servers to plugins
- Test plugins locally using the `--plugin-dir` flag
- Debug common plugin development issues
- Organize complex plugins effectively

**Key Concepts:**
- Plugin directory structure and requirements
- Plugin manifest schema and required fields
- Component types: commands, skills, agents, hooks
- The critical mistake: not putting components inside `.claude-plugin/`
- Local testing workflow
- LSP server integration

**Content Outline:**
1. Plugin structure requirements
2. Creating the plugin manifest (`plugin.json`)
3. Adding components:
   - Commands (user-invoked)
   - Skills (model-invoked)
   - Agents
   - Hooks
   - MCP servers
   - LSP servers
4. Testing with `--plugin-dir`
5. Debugging techniques
6. Best practices for plugin organization
7. When to create custom LSP plugins

**Knowledge Check Questions:**

1. **Where should the `commands/` directory be located in a plugin?**
   - A) Inside `.claude-plugin/`
   - B) At the plugin root level
   - C) Inside a `src/` directory
   - D) Anywhere in the plugin
   
   **Answer:** B
   **Explanation:** This is a common mistake - only `plugin.json` goes inside `.claude-plugin/`. All other directories (`commands/`, `skills/`, `agents/`, `hooks/`) must be at the plugin root.

2. **What information is required in a plugin manifest file?**
   - A) name only
   - B) name, description, and version
   - C) name, version, author, and license
   - D) All metadata fields must be completed
   
   **Answer:** B
   **Explanation:** The required fields are `name`, `description`, and `version`. Other fields like `author`, `homepage`, and `license` are optional.

3. **How do you test a plugin during development without installing it?**
   - A) Run `/plugin test ./my-plugin`
   - B) Use `claude --plugin-dir ./my-plugin`
   - C) Copy it to `.claude/` temporarily
   - D) Install it with `--test` flag
   
   **Answer:** B
   **Explanation:** The `--plugin-dir` flag loads a plugin directly from a local directory for testing without installation.

4. **What is the difference between commands and skills in a plugin?**
   - A) Commands are for users, skills are for Claude
   - B) Commands are faster than skills
   - C) Skills require more configuration than commands
   - D) Commands can use arguments but skills cannot
   
   **Answer:** A
   **Explanation:** Commands are user-invoked with slash commands (like `/my-plugin:hello`), while skills are model-invoked by Claude based on task context.

---

## Module 7: Lab - Creating Your First Plugin

**Duration:** 45 minutes

**Learning Objectives:**
By the end of this lab, learners will be able to:
- Create a complete plugin from scratch
- Write a properly formatted plugin manifest
- Add skills with frontmatter and instructions
- Use skill arguments with the `$ARGUMENTS` placeholder
- Test plugins locally

**Lab Steps:**
1. Create plugin directory: `mkdir my-first-plugin`
2. Create `.claude-plugin` directory and `plugin.json` manifest
3. Create `skills/hello` directory structure
4. Write `SKILL.md` with proper frontmatter
5. Test with `claude --plugin-dir ./my-first-plugin`
6. Add `$ARGUMENTS` support for dynamic greetings
7. Restart and retest with personalized input

**Expected Outcomes:**
- Working plugin with custom skill
- Can invoke skill with `/my-first-plugin:hello`
- Skill responds to arguments properly
- Understands the development iteration cycle

**Knowledge Check Questions:**

1. **What is the correct file path for a skill named "hello" in a plugin named "my-first-plugin"?**
   - A) `my-first-plugin/.claude-plugin/skills/hello.md`
   - B) `my-first-plugin/skills/hello/SKILL.md`
   - C) `my-first-plugin/commands/hello.md`
   - D) `my-first-plugin/skills/hello.md`
   
   **Answer:** B
   **Explanation:** Skills live in `skills/[skill-name]/SKILL.md` at the plugin root, not inside `.claude-plugin/`.

2. **In the plugin manifest, the `name` field determines:**
   - A) Only the display name in the plugin manager
   - B) The namespace prefix for all plugin commands
   - C) The directory name where the plugin must be stored
   - D) The marketplace where the plugin will be published
   
   **Answer:** B
   **Explanation:** The `name` field becomes the namespace prefix (e.g., `"name": "greet"` creates commands like `/greet:hello`).

3. **What does the `$ARGUMENTS` placeholder do in a skill file?**
   - A) Defines the skill's required parameters
   - B) Captures all text the user types after the skill command
   - C) Creates command-line flags for the skill
   - D) Specifies the skill's return value
   
   **Answer:** B
   **Explanation:** `$ARGUMENTS` is replaced with any text the user provides after the command name, enabling dynamic skill behavior.

4. **After modifying a plugin file during development, what must you do to see the changes?**
   - A) Run `/plugin reload`
   - B) Restart Claude Code
   - C) Run `/refresh`
   - D) Changes apply automatically
   
   **Answer:** B
   **Explanation:** You need to restart Claude Code to pick up changes to plugin files during development.

---

## Module 8: Converting Configurations to Plugins

**Duration:** 30 minutes

**Learning Objectives:**
By the end of this module, learners will be able to:
- Identify when to convert standalone configurations to plugins
- Execute the migration workflow systematically
- Adapt hooks from settings.json format to hooks.json format
- Verify migrated plugins work correctly
- Maintain both versions during transition if needed

**Key Concepts:**
- Migration triggers and decision points
- File location mapping (`.claude/` → plugin structure)
- Hooks conversion process
- Testing migrated plugins
- Removing duplicate configurations

**Content Outline:**
1. When to convert to plugins
2. Migration workflow:
   - Create plugin structure
   - Copy existing files
   - Migrate hooks configuration
   - Test and verify
3. What changes during migration
4. Handling the transition period
5. Cleanup after successful migration

**Knowledge Check Questions:**

1. **What is the primary difference in hooks configuration between standalone and plugin formats?**
   - A) Plugins use YAML instead of JSON
   - B) Standalone uses settings.json, plugins use hooks/hooks.json
   - C) Plugins require different hook event names
   - D) Standalone hooks are more powerful
   
   **Answer:** B
   **Explanation:** Standalone configurations put hooks in `.claude/settings.json` or `settings.local.json`, while plugins use a dedicated `hooks/hooks.json` file.

2. **When migrating commands from `.claude/` to a plugin, where should they be placed?**
   - A) `plugin-name/.claude-plugin/commands/`
   - B) `plugin-name/commands/`
   - C) `plugin-name/src/commands/`
   - D) `plugin-name/.claude/commands/`
   
   **Answer:** B
   **Explanation:** Commands go in the `commands/` directory at the plugin root, not inside `.claude-plugin/`.

3. **After successfully migrating configurations to a plugin, what should you do with the original `.claude/` files?**
   - A) Leave them as backup
   - B) Delete them immediately
   - C) Remove them to avoid duplicates, as the plugin version takes precedence
   - D) Keep both to have options
   
   **Answer:** C
   **Explanation:** The documentation recommends removing original files after migration to avoid duplicates, since loaded plugins take precedence anyway.

---

## Module 9: Lab - Converting Hooks to Plugins

**Duration:** 30 minutes

**Learning Objectives:**
By the end of this lab, learners will be able to:
- Create plugin structure from existing configurations
- Copy configuration files to the plugin structure
- Convert hooks from settings.json to hooks.json format
- Test the migrated plugin to ensure functionality
- Verify all components work in the new plugin format

**Lab Steps:**
1. Create plugin directory structure with `.claude-plugin/`
2. Write plugin manifest
3. Copy existing commands, agents, and skills from `.claude/`
4. Create `hooks/` directory
5. Extract hooks configuration from settings.json
6. Adapt hooks format (using jq for file path extraction in examples)
7. Test with `claude --plugin-dir ./my-plugin`
8. Verify all components function correctly

**Expected Outcomes:**
- All existing functionality now available in plugin format
- Hooks trigger correctly
- Can share plugin with team
- Original configurations safely migrated

**Knowledge Check Questions:**

1. **What command structure do hooks use to receive input in the plugin format?**
   - A) Direct command-line arguments
   - B) JSON on stdin (e.g., using jq to extract values)
   - C) Environment variables
   - D) Configuration files
   
   **Answer:** B
   **Explanation:** The example shows hooks receive input as JSON on stdin and use tools like `jq` to extract specific fields like `tool_input.file_path`.

2. **In the example hook for linting after file edits, what does the `matcher` field do?**
   - A) Specifies which files to lint
   - B) Filters which tools trigger the hook (e.g., "Write|Edit")
   - C) Defines the linting pattern to search for
   - D) Sets the hook priority
   
   **Answer:** B
   **Explanation:** The `matcher` field uses a pattern to determine which tool invocations trigger the hook, in this case "Write|Edit" operations.

3. **What is the correct plugin structure for hooks?**
   - A) `hooks.json` at plugin root
   - B) `.claude-plugin/hooks.json`
   - C) `hooks/hooks.json`
   - D) `config/hooks.json`
   
   **Answer:** C
   **Explanation:** Hooks go in a dedicated `hooks/` directory with a `hooks.json` file, following the plugin structure requirements.

---

## Course Completion

**Final Assessment:**
Upon completing all modules and labs, learners should be able to:
- Discover and evaluate plugins from marketplaces
- Install and manage plugins across different scopes
- Create custom plugins with skills, agents, and hooks
- Test and debug plugin functionality
- Convert existing configurations to shareable plugins
- Distribute plugins through marketplaces

**Next Steps:**
- Explore the official plugin marketplace
- Create custom plugins for your team's workflows
- Contribute to the Claude Code plugin ecosystem
- Set up your own plugin marketplace for distribution

**Additional Resources:**
- Claude Code Plugin Documentation: https://docs.claude.com
- Plugin Reference Guide: https://docs.claude.com/en/plugins-reference
- Skills Documentation: https://docs.claude.com/en/skills
- MCP Server Documentation: https://docs.anthropic.com/mcp

---

## Assessment Answer Key

### Module 1
1. B - Sharing with team is the primary plugin use case
2. B - Namespacing prevents conflicts
3. B - Start standalone, convert later
4. A, B, C, D - All are valid plugin components

### Module 2
1. B - `/plugin` opens the manager
2. C - Discover tab shows available plugins
3. B - Check homepage before installing

### Module 3
1. C - Full command path is required
2. B - Plugins appear in Discover tab
3. B - Shift+Tab navigates backward

### Module 4
1. C - CLI defaults to user scope
2. B - Project scope adds to settings.json
3. C - Local scope for isolated testing
4. B - Disabling is temporary

### Module 5
1. B - Namespaced command format
2. C - Check Discover tab or run /help
3. B - Managed = administrator-controlled

### Module 6
1. B - Components go at plugin root
2. B - Name, description, version required
3. B - Use --plugin-dir flag
4. A - Commands for users, skills for Claude

### Module 7
1. B - Skills use directory/SKILL.md structure
2. B - Name field creates namespace
3. B - $ARGUMENTS captures user input
4. B - Must restart Claude Code

### Module 8
1. B - Different file locations
2. B - Commands at plugin root
3. C - Remove originals to avoid duplicates

### Module 9
1. B - JSON on stdin
2. B - Matcher filters tool invocations
3. C - hooks/hooks.json structure
