# 🇺🇸 Covfefe

> _"We merge, folks. We always merge — the best merges, nobody merges like us, believe me. It's gonna be tremendous."_

A cross-agent persona — built on the [Agent Skills](https://agentskills.io) standard — that bids your coding agent speak like Donald J. Trump: tremendous, superlative-laden, totally confident, for every turn of every session, on any topic. Works with Claude Code, Codex CLI, Gemini CLI, Cursor, Windsurf, Cline, Copilot, and any other agent that reads a Markdown rule file.

Technical advice stays 100% correct. Only the prose around it goes big league.

<p align="center">
  <img src="assets/make-agents-great-again.webp" alt="Make Agents Great Again" width="320">
</p>

> Inspired by the most famous typo in the history of typos. Nobody knows what it means, but it's tremendous.

## Sample

```
$ /covfefe

> Look, `fetchUser` returns a Promise — a beautiful Promise,
> one of the best — but you never await it. So `user` isn't
> the data, folks, it's an empty Promise object. Nothing in
> it. Put `await` in front, and believe me, the data is
> yours. Easy fix. Tremendous.
```

## Install

For the full per-agent install matrix, see [INSTALL.md](INSTALL.md). The short version:

| Agent | How |
| --- | --- |
| Claude Code | `/plugin marketplace add paccodes/covfefe` then `/plugin install covfefe@covfefe` |
| Codex CLI (and anything reading `AGENTS.md`) | Drop [`AGENTS.md`](AGENTS.md) into your project root |
| Gemini CLI | `gemini extensions install https://github.com/paccodes/covfefe` |
| Cursor / Windsurf / Cline / Copilot | `npx skills add paccodes/covfefe -a <agent>` |

## Usage

- **Always on**: once installed, the agent talks like Donald J. Trump from the very first turn of every session, on any topic — technical or otherwise.
- **Manually (Claude Code)**: type `/covfefe` at any time to summon him if he's somehow gone quiet.
- **To exit**: ask for `plain english`, `normal mode`, `be serious`, or simply `drop the voice`. The agent returns to its workaday register without ceremony — no farewell rally.

## What stays literal

Identifiers, file paths, shell commands, error messages, version numbers, and anything in backticks are never restyled. Covfefe is a costume for the prose, not a translator for the code.

```
✓ "Your `useReducer` has a stale closure over `count`. Not good."
✗ "Your `useTremendousReducer` has a stale closure over `bigLeagueCount`."
```

## Repo layout

```
covfefe/
├── .claude-plugin/
│   └── marketplace.json               # Claude Code plugin marketplace entry
├── .github/
│   └── workflows/                     # CI — validates SKILL.md frontmatter on PRs
│       ├── lint-skill.yml
│       └── validate_skill.py
├── assets/                            # images and other static assets
├── commands/
│   └── covfefe.md                     # /covfefe slash command (Claude Code)
├── skills/
│   └── covfefe/                       # canonical skill (source of truth)
│       ├── examples.md                # before/after exchanges
│       ├── glossary.md                # jargon → Trump-ism translations
│       └── SKILL.md                   # persona + standing instructions
├── AGENTS.md                          # autodiscovery file for Codex CLI and AGENTS.md-aware agents
├── CONTRIBUTING.md
├── gemini-extension.json              # Gemini CLI extension manifest
├── GEMINI.md                          # context file loaded by the Gemini CLI extension
├── INSTALL.md                         # per-agent install matrix
├── LICENSE
└── README.md
```

Cursor, Windsurf, Cline, Copilot, and the long tail of other agents are reached through the upstream [`skills`](https://github.com/vercel-labs/skills) CLI rather than committed mirror files — see [INSTALL.md](INSTALL.md).

## Contributing

Pull requests for new glossary entries, exemplars, or voice refinements are most welcome. Keep additions terse and technically accurate. A punchy line that misleads is worse than no line at all. Believe me. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

## Disclaimer

A parody persona for fun. Not affiliated with, endorsed by, or representing any real person. The code advice is real; the bravado is satire.

## License

MIT. See [LICENSE](LICENSE).
