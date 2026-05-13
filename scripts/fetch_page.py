#!/usr/bin/env python3
"""Fetch JS-rendered page, expanding all Streamlit expanders."""

import argparse
import re
import time
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright


def fetch_page(url: str, output: str | None = None, timeout: int = 60000) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=timeout)
        time.sleep(4)
        page.wait_for_load_state("networkidle", timeout=timeout)

        # Click all expander arrows to reveal hidden content
        expanders = page.locator(
            'button[data-testid="stExpanderToggleIcon"], '
            'button[kind="secondary"] svg, '
            '.st-expander svg, '
            'svg[data-icon="chevron-right"], '
            'svg[data-icon="chevron-down"]'
        )
        count = expanders.count()
        for i in range(count):
            try:
                expanders.nth(i).click()
                time.sleep(0.5)
            except Exception:
                pass

        time.sleep(2)

        title = page.title()
        content = page.inner_text("body")

        browser.close()

    safe_title = re.sub(r"[^a-zA-Z0-9]+", "-", title).strip("-").lower() or "untitled"
    ts = datetime.now().strftime("%Y-%m%d-%H%M%S")
    filename = f"{ts}_{safe_title[:60]}.md"

    md = f"# {title}\n\nURL: {url}\nData: {datetime.now().isoformat()}\n\n---\n\n{content}"

    if output:
        outpath = Path(output)
        if outpath.is_dir():
            outpath = outpath / filename
        outpath.parent.mkdir(parents=True, exist_ok=True)
        outpath.write_text(md, encoding="utf-8")
        print(f"Saved: {outpath}")
    else:
        print(md)

    return md


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch JS-rendered page with expanders")
    parser.add_argument("url", help="Page URL to fetch")
    parser.add_argument("-o", "--output", help="Output file or directory")
    parser.add_argument("-t", "--timeout", type=int, default=60000, help="Timeout in ms")
    args = parser.parse_args()

    fetch_page(args.url, args.output, args.timeout)
