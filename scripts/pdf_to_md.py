#!/usr/bin/env python3
"""Convert a PDF to Markdown text. Uses pandoc as primary engine, falls back to pdftotext."""

import argparse
import subprocess
import sys
from pathlib import Path


def pdf_to_md(pdf_path: str, output: str | None = None) -> str:
    inp = Path(pdf_path)
    if not inp.exists():
        print(f"Error: file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    # Try pandoc first
    md = None
    try:
        result = subprocess.run(
            ["pandoc", str(inp), "-t", "markdown", "--wrap=preserve"],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode == 0 and result.stdout.strip():
            md = result.stdout
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Fallback to pdftotext
    if not md:
        try:
            result = subprocess.run(
                ["pdftotext", str(inp), "-", "-layout"],
                capture_output=True, text=True, timeout=120
            )
            if result.returncode == 0 and result.stdout.strip():
                md = result.stdout
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

    if not md:
        print("Error: no converter available (pandoc or pdftotext required)", file=sys.stderr)
        sys.exit(1)

    md = md.strip()

    if output:
        outpath = Path(output)
        if outpath.is_dir():
            stem = inp.stem.replace(" ", "-").lower()
            outpath = outpath / f"{stem}.md"
        outpath.parent.mkdir(parents=True, exist_ok=True)
        outpath.write_text(md, encoding="utf-8")
        print(f"Saved: {outpath} ({len(md)} chars)")
    else:
        print(md)

    return md


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown")
    parser.add_argument("pdf", help="PDF file path")
    parser.add_argument("-o", "--output", help="Output file or directory")
    args = parser.parse_args()
    pdf_to_md(args.pdf, args.output)
