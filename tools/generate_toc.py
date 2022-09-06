#!/usr/bin/env python3

from pathlib import Path
import re

base_dir = Path(__file__).resolve().parent.parent

toc_path = base_dir / "content/00-toc.md"

src_files = [
    "01-introduction.md",
    "02-contributions-to-existing-projects.md",
    "03-starting-oss-projects.md",
    "04-references.md",
    "05-appendix.md"
]

toc = "# Outbound Open Source: Leveraging open source ecosystems\n\n"
toc += "---\n"

for src_file in src_files:
    with (base_dir / "content" / src_file).open() as f:
        for line in f:
            m = re.search("^(#+) (.*)", line)
            if m:
                prefix = m.group(1)
                title = m.group(2)
                if prefix == "#":
                    toc += f"\n## [{title}]({src_file})\n\n"
                else:
                    toc += "  " * (len(prefix) - 2)
                    toc += f"* {title}\n"

with toc_path.open("w") as f:
    f.write(toc)
