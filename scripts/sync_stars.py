#!/usr/bin/env python3
"""
Sync GitHub star counts + align all tables in README.md.
Extracts repo URLs from table rows, queries GitHub API for stars,
updates Star columns, then pads all table columns for visual alignment.
Commits and pushes if changed.
"""

import re
import os
import sys
import time
import unicodedata
import urllib.request
import urllib.error
import json
import subprocess

REPO_DIR = os.path.expanduser("~/app/engineering-skill-hub")
README_PATH = os.path.join(REPO_DIR, "README.md")


def get_github_token():
    creds_path = os.path.expanduser("~/.git-credentials")
    with open(creds_path) as f:
        line = f.read().strip()
    # Format: https://user:token@github.com — match after user:
    match = re.search(r'//[^:]+:([^@]+)@github\.com', line)
    return match.group(1) if match else None


def display_width(s):
    """Get display width considering CJK double-width chars."""
    w = 0
    for ch in s:
        if unicodedata.east_asian_width(ch) in ('W', 'F'):
            w += 2
        else:
            w += 1
    return w


def pad_to_width(s, target):
    """Pad string with spaces to reach target display width."""
    cur = display_width(s)
    return s + ' ' * max(0, target - cur)


def query_stars(owner, repo, token, retries=2):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "engineering-skill-hub-sync"
    }
    if token:
        headers["Authorization"] = f"token {token}"

    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
                return data.get("stargazers_count")
        except urllib.error.HTTPError as e:
            if e.code == 403:
                reset = e.headers.get("X-RateLimit-Reset")
                if reset and attempt < retries:
                    wait = max(int(reset) - int(time.time()), 5)
                    print(f"  Rate limited, waiting {min(wait, 60)}s...")
                    time.sleep(min(wait, 60))
                    continue
                print(f"  403 rate limited: {owner}/{repo}")
                return None
            elif e.code == 404:
                print(f"  404: {owner}/{repo}")
                return None
            else:
                print(f"  HTTP {e.code}: {owner}/{repo}")
                return None
        except Exception as e:
            print(f"  Error: {e}")
            if attempt < retries:
                time.sleep(2)
                continue
            return None
    return None


def sync_stars(content, token):
    """Update star counts in table rows. Returns (new_content, updated_count)."""
    lines = content.split("\n")
    github_url_pattern = re.compile(r'https://github\.com/([^/\s"]+)/([^/\s")\]]+)')

    # Collect unique repos
    repos = set()
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        for m in github_url_pattern.finditer(line):
            owner, repo = m.group(1), m.group(2)
            if not (owner == "Zehebi29" and repo == "engineering-skill-hub"):
                repos.add((owner, repo))

    print(f"Found {len(repos)} unique repos to sync")

    # Query stars
    stars_map = {}
    for idx, (owner, repo) in enumerate(sorted(repos)):
        print(f"  [{idx+1}/{len(repos)}] {owner}/{repo}...", end=" ")
        stars = query_stars(owner, repo, token)
        if stars is not None:
            stars_map[(owner, repo)] = stars
            print(f"⭐ {stars}")
        else:
            print("skipped")
        if idx < len(repos) - 1:
            time.sleep(0.8)

    # Update star values in table rows
    updated = 0
    new_lines = []
    for line in lines:
        if not line.strip().startswith("|"):
            new_lines.append(line)
            continue

        # Find repos on this line
        line_repos = []
        for m in github_url_pattern.finditer(line):
            key = (m.group(1), m.group(2))
            if key in stars_map:
                line_repos.append(key)

        if line_repos:
            owner, repo = line_repos[-1]
            new_stars = stars_map[(owner, repo)]
            # Replace last | number | at end of line
            match = re.search(r'(\|\s*)(\d+)(\s*\|)\s*$', line)
            if match:
                old_stars = int(match.group(2))
                if old_stars != new_stars:
                    line = line[:match.start()] + f"{match.group(1)}{new_stars}{match.group(3)}"
                    updated += 1
                    print(f"  {owner}/{repo}: {old_stars} → {new_stars}")

        new_lines.append(line)

    print(f"\nStar sync: {updated} updated")
    return "\n".join(new_lines), updated


def align_tables(content):
    """Pad all markdown table columns to equal width for visual alignment."""
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        # Detect table start: line starts with | and next line is separator
        if (lines[i].strip().startswith("|") and
            i + 1 < len(lines) and
            re.match(r'\|[\s\-:|]+\|', lines[i + 1].strip())):

            # Collect all table lines
            table_start = i
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1

            # Parse cells
            parsed = []
            for tl in table_lines:
                # Split by | but keep structure
                cells = tl.split("|")
                # cells[0] is before first | (empty), cells[-1] is after last | (empty or newline)
                # Inner cells are the actual content
                if len(cells) >= 3:
                    inner = cells[1:-1]
                    parsed.append(inner)

            if not parsed:
                result.extend(table_lines)
                continue

            # Check if this is a separator row
            def is_separator(cells):
                return all(re.match(r'^[\s\-:]+$', c) for c in cells)

            # Calculate max width per column (skip separator rows)
            num_cols = max(len(row) for row in parsed)
            col_widths = [0] * num_cols
            for row_idx, row in enumerate(parsed):
                if is_separator(row):
                    continue
                for col_idx, cell in enumerate(row):
                    if col_idx < num_cols:
                        col_widths[col_idx] = max(col_widths[col_idx], display_width(cell.strip()))

            # Rebuild table with padding
            for row_idx, row in enumerate(parsed):
                if is_separator(row):
                    # Rebuild separator with proper width
                    new_cells = []
                    for col_idx in range(num_cols):
                        if col_idx < len(row):
                            sep = row[col_idx].strip()
                            # Preserve alignment markers (:---:, :---, ---:)
                            if ':' in sep:
                                # Keep the colons, pad dashes
                                left = sep.startswith(':')
                                right = sep.endswith(':')
                                dash_count = max(3, col_widths[col_idx])
                                s = ':' + '-' * (dash_count - 2) + ':' if left and right else \
                                    ':' + '-' * (dash_count - 1) if left else \
                                    '-' * (dash_count - 1) + ':' if right else \
                                    '-' * dash_count
                                new_cells.append(s)
                            else:
                                new_cells.append('-' * max(3, col_widths[col_idx]))
                        else:
                            new_cells.append('---')
                    result.append('| ' + ' | '.join(new_cells) + ' |')
                else:
                    new_cells = []
                    for col_idx in range(num_cols):
                        if col_idx < len(row):
                            cell = row[col_idx].strip()
                            padded = pad_to_width(cell, col_widths[col_idx])
                            new_cells.append(padded)
                        else:
                            new_cells.append('')
                    result.append('| ' + ' | '.join(new_cells) + ' |')
        else:
            result.append(lines[i])
            i += 1

    return "\n".join(result)


def main():
    token = get_github_token()
    if not token:
        print("ERROR: Could not extract GitHub token")
        sys.exit(1)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Step 1: Sync stars
    content, star_updates = sync_stars(content, token)

    # Step 2: Align tables
    content = align_tables(content)

    # Write
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    # Git commit & push
    os.chdir(REPO_DIR)
    subprocess.run(["git", "add", "README.md"], check=True)

    result = subprocess.run(["git", "diff", "--cached", "--quiet"], capture_output=True)
    if result.returncode == 0:
        print("\nNo changes. Already up to date.")
        return

    msg = f"chore: sync star counts ({star_updates} updated) + align tables" if star_updates else "chore: align tables"
    subprocess.run(["git", "commit", "-m", msg], check=True)
    subprocess.run(["git", "push"], check=True)
    print(f"\nDone ✓ — {msg}")


if __name__ == "__main__":
    main()
