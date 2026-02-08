Module Title: PLab: Adding a Demo Plugin

Description: Install a plugin from the demo marketplace.

# Introduction

This lab walks you through creating a plugin and its various compenents: directory, manifest, skill, tests, and skill arguments.

## Steps

<Steps>
  <Step title="Create the plugin directory">
    Every plugin lives in its own directory containing a manifest and your skills, agents, or hooks. Create one now:

    ```bash  theme={null}
    mkdir my-first-plugin
    ```
  </Step>

  <Step title="Create the plugin manifest">
    The manifest file at `.claude-plugin/plugin.json` defines your plugin's identity: its name, description, and version. Claude Code uses this metadata to display your plugin in the plugin manager.

    Create the `.claude-plugin` directory inside your plugin folder:

    ```bash  theme={null}
    mkdir my-first-plugin/.claude-plugin
    ```

    Then create `my-first-plugin/.claude-plugin/plugin.json` with this content:

    ```json my-first-plugin/.claude-plugin/plugin.json theme={null}
    {
    "name": "my-first-plugin",
    "description": "A greeting plugin to learn the basics",
    "version": "1.0.0",
    "author": {
    "name": "Your Name"
    }
    }
    ```

    | Field         | Purpose                                                                                                |
    | :------------ | :----------------------------------------------------------------------------------------------------- |
    | `name`        | Unique identifier and skill namespace. Skills are prefixed with this (e.g., `/my-first-plugin:hello`). |
    | `description` | Shown in the plugin manager when browsing or installing plugins.                                       |
    | `version`     | Track releases using [semantic versioning](/en/plugins-reference#version-management).                  |
    | `author`      | Optional. Helpful for attribution.                                                                     |

    For additional fields like `homepage`, `repository`, and `license`, see the [full manifest schema](/en/plugins-reference#plugin-manifest-schema).
  </Step>

  <Step title="Add a skill">
    Skills live in the `skills/` directory. Each skill is a folder containing a `SKILL.md` file. The folder name becomes the skill name, prefixed with the plugin's namespace (`hello/` in a plugin named `my-first-plugin` creates `/my-first-plugin:hello`).

    Create a skill directory in your plugin folder:

    ```bash  theme={null}
    mkdir -p my-first-plugin/skills/hello
    ```

    Then create `my-first-plugin/skills/hello/SKILL.md` with this content:

    ```markdown my-first-plugin/skills/hello/SKILL.md theme={null}
    ---
    description: Greet the user with a friendly message
    disable-model-invocation: true
    ---

    Greet the user warmly and ask how you can help them today.
    ```
  </Step>

  <Step title="Test your plugin">
    Run Claude Code with the `--plugin-dir` flag to load your plugin:

    ```bash  theme={null}
    claude --plugin-dir ./my-first-plugin
    ```

    Once Claude Code starts, try your new command:

    ```shell  theme={null}
    /my-first-plugin:hello
    ```

    You'll see Claude respond with a greeting. Run `/help` to see your command listed under the plugin namespace.

    <Note>
      **Why namespacing?** Plugin skills are always namespaced (like `/greet:hello`) to prevent conflicts when multiple plugins have skills with the same name.

      To change the namespace prefix, update the `name` field in `plugin.json`.
    </Note>
  </Step>

  <Step title="Add skill arguments">
    Make your skill dynamic by accepting user input. The `$ARGUMENTS` placeholder captures any text the user provides after the skill name.

    Update your `hello.md` file:

    ```markdown my-first-plugin/commands/hello.md theme={null}
    ---
    description: Greet the user with a personalized message
    ---

    # Hello Command

    Greet the user named "$ARGUMENTS" warmly and ask how you can help them today. Make the greeting personal and encouraging.
    ```

    Restart Claude Code to pick up the changes, then try the command with your name:

    ```shell  theme={null}
    /my-first-plugin:hello Alex
    ```

    Claude will greet you by name. For more on passing arguments to skills, see [Skills](/en/skills#pass-arguments-to-skills).
  </Step>
</Steps>

You've successfully created and tested a plugin with these key components:

* **Plugin manifest** (`.claude-plugin/plugin.json`): describes your plugin's metadata
* **Commands directory** (`commands/`): contains your custom skills
* **Skill arguments** (`$ARGUMENTS`): captures user input for dynamic behavior

<Tip>
  The `--plugin-dir` flag is useful for development and testing. When you're ready to share your plugin with others, see [Create and distribute a plugin marketplace](/en/plugin-marketplaces).
</Tip>