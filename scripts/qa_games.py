#!/usr/bin/env python3
"""Free static QA checks for Daddy's Game Workshop HTML games.

Uses Python + Node already available on GitHub-hosted runners.
No npm packages, paid APIs, or external services are required.
"""

from __future__ import annotations

import html.parser
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
GAMES = ROOT / "games"

ERRORS: list[str] = []
WARNINGS: list[str] = []


class TagCounter(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        self.tags.append(tag.lower())


def rel(path: pathlib.Path) -> str:
    return str(path.relative_to(ROOT))


def error(path: pathlib.Path, message: str) -> None:
    ERRORS.append(f"{rel(path)}: {message}")


def warn(path: pathlib.Path, message: str) -> None:
    WARNINGS.append(f"{rel(path)}: {message}")


def check_inline_js(path: pathlib.Path, text: str) -> None:
    # Only inspect inline scripts. External script URLs are reported separately.
    scripts = re.findall(
        r"<script\b(?![^>]*\bsrc\s*=)[^>]*>(.*?)</script\s*>",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    for number, script in enumerate(scripts, start=1):
        # Skip non-JavaScript data blocks.
        opening_matches = list(
            re.finditer(
                r"<script\b(?![^>]*\bsrc\s*=)[^>]*>",
                text,
                flags=re.IGNORECASE,
            )
        )
        if number <= len(opening_matches):
            opening = opening_matches[number - 1].group(0).lower()
            if "application/json" in opening or "application/ld+json" in opening:
                continue

        with tempfile.NamedTemporaryFile(
            "w", suffix=".js", encoding="utf-8", delete=False
        ) as handle:
            handle.write(script)
            temp_name = handle.name
        proc = subprocess.run(
            ["node", "--check", temp_name],
            capture_output=True,
            text=True,
            check=False,
        )
        pathlib.Path(temp_name).unlink(missing_ok=True)
        if proc.returncode != 0:
            detail = (proc.stderr or proc.stdout).strip().splitlines()
            short = " | ".join(detail[-3:]) if detail else "node --check failed"
            error(path, f"inline script #{number} has JavaScript syntax errors: {short}")


def check_file(path: pathlib.Path) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        error(path, "is not UTF-8 text")
        return

    lower = text.lower()

    if len(text.strip()) < 20:
        warn(path, "is almost empty; this may be a placeholder/landing file")
        return

    if "<!doctype html" not in lower:
        error(path, "missing <!DOCTYPE html>")
    if "<html" not in lower or "</html>" not in lower:
        error(path, "missing opening/closing <html> tags")
    if "<body" not in lower or "</body>" not in lower:
        error(path, "missing opening/closing <body> tags")
    if "<title" not in lower:
        error(path, "missing <title>")
    if 'name="viewport"' not in lower and "name='viewport'" not in lower:
        error(path, "missing mobile viewport meta tag")

    if lower.count("<script") != lower.count("</script>"):
        error(path, "script tag count does not match")

    parser = TagCounter()
    try:
        parser.feed(text)
    except Exception as exc:
        error(path, f"HTML parser error: {exc}")

    external_scripts = re.findall(
        r"<script\b[^>]*\bsrc\s*=\s*['\"](https?://[^'\"]+)",
        text,
        flags=re.IGNORECASE,
    )
    for url in external_scripts:
        warn(path, f"uses external script dependency: {url}")

    paid_api_terms = [
        "api.openai.com",
        "generativelanguage.googleapis.com",
        "api.x.ai",
        "tripo3d",
    ]
    for term in paid_api_terms:
        if term in lower:
            warn(path, f"contains possible paid/external API reference: {term}")

    check_inline_js(path, text)


def main() -> int:
    if not GAMES.exists():
        print("games/ folder not found", file=sys.stderr)
        return 1

    files = sorted(GAMES.rglob("index.html"))
    if not files:
        print("No game index.html files found", file=sys.stderr)
        return 1

    print(f"Checking {len(files)} HTML files...")
    for path in files:
        check_file(path)

    if WARNINGS:
        print("\nWARNINGS")
        for item in WARNINGS:
            print(f"  - {item}")

    if ERRORS:
        print("\nERRORS")
        for item in ERRORS:
            print(f"  - {item}")
        print(f"\nQA FAILED: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s).")
        return 1

    print(f"\nQA PASSED: {len(files)} files checked, {len(WARNINGS)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
