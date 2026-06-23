# Contributing to Covfefe

Pull requests for new glossary entries, exemplars, or voice refinements are most welcome — tremendous, frankly. Keep additions terse and technically accurate. A punchy line that misleads is worse than no line at all. Believe me.

## What to contribute

- **Glossary entries** ([`skills/covfefe/glossary.md`](skills/covfefe/glossary.md)) — canonical Trump-ism renderings of technical jargon. One row per term; lean on the formulas already present (superlatives, scale-and-credibility tics, stamps).
- **Exemplars** ([`skills/covfefe/examples.md`](skills/covfefe/examples.md)) — before/after pairs for common technical exchanges (bug reports, reviews, PR summaries). Plain version first, Covfefe version second.
- **Voice refinements** ([`skills/covfefe/SKILL.md`](skills/covfefe/SKILL.md)) — sharpening or simplifying the standing rules. Changes here also belong in [`AGENTS.md`](AGENTS.md) and [`GEMINI.md`](GEMINI.md), which mirror the core ruleset for non-Claude agents.

## Voice guidelines

- **Identifiers, paths, commands, error messages, and anything in backticks are never restyled.** The voice is a costume for the prose, not a translator for the code. ALL CAPS is for prose only — case is meaningful in code. See [`SKILL.md`](skills/covfefe/SKILL.md) for the full literal-tokens list.
- **Terse beats bloated.** A bug report stays one or two sentences — merely gone big league. No rambling rallies, no ten-minute riffs, unless the exemplar is explicitly about that.
- **Sparing stamps.** `Sad!`, `Not good!`, `Tremendous!`, `believe me` are seasoning, not every sentence.

## Submitting

1. Fork, branch, edit.
2. Run the linter locally if you touched the skill or marketplace manifest:
   ```bash
   python .github/workflows/validate_skill.py
   python -c "import json; json.load(open('.claude-plugin/marketplace.json'))"
   ```
3. Open a pull request. CI runs the same checks on every PR.

## License

By contributing, you agree that your contributions shall be licensed under the [MIT License](LICENSE) that covers this project.
