# Installing Covfefe

Covfefe ships as a single skill (`skills/covfefe/`) with thin adapter files at the repo root for agents that look elsewhere for their persona instructions. Pick the section that matches your agent.

## Claude Code

### As a plugin marketplace (recommended)

```
/plugin marketplace add paccodes/covfefe
/plugin install covfefe@covfefe
```

This installs both the skill and the `/covfefe` slash command (defined in [`commands/covfefe.md`](commands/covfefe.md)) for summoning the Donald mid-session if the voice goes quiet.

### As a personal skill (no plugin)

```bash
git clone https://github.com/paccodes/covfefe.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/covfefe/skills/covfefe" ~/.claude/skills/covfefe
```

Restart Claude Code (or wait — skill directories are live-watched once present). The `/covfefe` slash command is not registered in this mode; ask Claude for "covfefe" by name instead, or use the plugin install above.

### As a project skill

Copy `skills/covfefe/` into your project's `.claude/skills/` directory. (Same caveat as the personal-skill mode: no `/covfefe` slash command — use the plugin install for that.)

## Codex CLI (and any agent that reads `AGENTS.md`)

Drop the `AGENTS.md` from this repo into the root of your project. Codex CLI auto-loads it on every session.

```bash
curl -fsSL https://raw.githubusercontent.com/paccodes/covfefe/main/AGENTS.md -o AGENTS.md
```

If you already maintain an `AGENTS.md`, append Covfefe's content to it under a `## Covfefe` heading.

## Gemini CLI

This repo is a valid Gemini CLI extension — `gemini-extension.json` points at `GEMINI.md`. Install it as an extension:

```bash
gemini extensions install https://github.com/paccodes/covfefe
```

Or, for a one-off project, drop `GEMINI.md` into the project root and Gemini CLI will pick it up.

## Cursor, Windsurf, Cline, Copilot, and 40+ other agents

The cleanest cross-agent distribution path is the upstream [`skills`](https://github.com/vercel-labs/skills) CLI, which knows how to write the right rule file into the right location for each agent:

```bash
# Cursor
npx skills add paccodes/covfefe -a cursor

# Windsurf
npx skills add paccodes/covfefe -a windsurf

# Cline
npx skills add paccodes/covfefe -a cline

# GitHub Copilot
npx skills add paccodes/covfefe -a github-copilot
```

See [`skills` agent profiles](https://github.com/vercel-labs/skills#supported-agents) for the full list (Junie, Trae, Warp, Tabnine, Replit, opencode, OpenHands, and more).

## Anywhere else

Any agent that reads a single Markdown context file from the project root will work — point it at `skills/covfefe/SKILL.md`, or copy the contents of `AGENTS.md` into whatever filename your agent expects.

## Uninstalling

- **Plugin marketplace**: `/plugin uninstall covfefe`
- **Personal skill**: `rm ~/.claude/skills/covfefe`
- **`npx skills`**: `npx skills remove paccodes/covfefe -a <agent>`
- **Adapter files**: delete the `AGENTS.md` / `GEMINI.md` / `gemini-extension.json` you copied in.
