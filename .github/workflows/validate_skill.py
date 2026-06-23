"""Validate every SKILL.md under skills/ has well-formed frontmatter."""

import sys
import yaml

from pathlib import Path

REQUIRED_FIELDS = ["description"]
SKILLS_DIR = Path("skills")


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        raise ValueError("missing opening '---' delimiter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing closing '---' delimiter")
    return yaml.safe_load(text[4:end]) or {}


def main() -> int:
    errors: list[str] = []
    skill_files = list(SKILLS_DIR.rglob("SKILL.md"))

    if not skill_files:
        print(f"no SKILL.md files found under {SKILLS_DIR}/", file=sys.stderr)
        return 1

    for path in skill_files:
        try:
            frontmatter = parse_frontmatter(path.read_text())
        except ValueError as error:
            errors.append(f"{path}: {error}")
            continue

        for field in REQUIRED_FIELDS:
            if field not in frontmatter:
                errors.append(f"{path}: missing required field '{field}'")

        description = frontmatter.get("description", "")
        if len(description) > 1536:
            errors.append(
                f"{path}: description exceeds 1536 chars ({len(description)})"
            )

        print(f"  ok  {path}")

    if errors:
        print("\nErrors:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    print(f"\n{len(skill_files)} skill(s) validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
