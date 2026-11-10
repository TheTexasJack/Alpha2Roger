"""Alpha2-Roger version check v0.1.

Every tracked file must carry a version, and VERSIONS.md must match the real version in each file.

Where a version lives, by file type:
  .md               a bold line near the top, like **Concept v0.61, 2026-11-10**
  .py               __version__ = "0.1"
  .json             a top-level "version" field
  .png .jpg .jpeg   _vN or _vN.N in the file name
  .gitignore        a comment line: # gitignore vN.N

Run:  python3 tools/version_check.py      (exit code 1 if anything is wrong)
"""
__version__ = "0.1"

import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def tracked_files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout
    return [ROOT / f for f in out.splitlines() if f]


def file_version(path):
    name = path.name
    suf = path.suffix.lower()
    try:
        if suf == ".md":
            m = re.search(r"\*\*[^*\n]*?\bv(\d+(?:\.\d+)*)\b", path.read_text(errors="ignore")[:600])
            return m and "v" + m.group(1)
        if suf == ".py":
            m = re.search(r'^__version__\s*=\s*"([\d.]+)"', path.read_text(errors="ignore"), re.M)
            return m and "v" + m.group(1)
        if suf == ".json":
            v = json.loads(path.read_text()).get("version")
            return v and "v" + str(v).lstrip("v")
        if suf in (".png", ".jpg", ".jpeg"):
            m = re.search(r"_v(\d+(?:\.\d+)*)", path.stem)
            return m and "v" + m.group(1)
        if name == ".gitignore":
            m = re.search(r"#\s*gitignore\s+v([\d.]+)", path.read_text())
            return m and "v" + m.group(1)
    except Exception as e:  # unreadable file counts as missing
        return None
    return "n/a"


def versions_table():
    rows = {}
    vf = ROOT / "VERSIONS.md"
    if vf.exists():
        for line in vf.read_text().splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 3 and cells[1].startswith("v"):
                rows[cells[0]] = cells[1]
    return rows


def check():
    problems, ok = [], 0
    table = versions_table()
    for path in tracked_files():
        rel = path.relative_to(ROOT).as_posix()
        v = file_version(path)
        if v == "n/a":
            continue
        if not v:
            problems.append(f"MISSING VERSION  {rel}")
            continue
        listed = table.get(rel)
        if listed is None:
            folder = next((k for k in table if k.endswith("/") and rel.startswith(k)), None)
            if folder is None:
                problems.append(f"NOT IN VERSIONS.md  {rel}  (file says {v})")
                continue
            ok += 1
            continue
        if listed != v:
            problems.append(f"MISMATCH  {rel}  file says {v}, VERSIONS.md says {listed}")
            continue
        ok += 1
    return ok, problems


if __name__ == "__main__":
    ok, problems = check()
    print(f"Version check v{__version__}: {ok} files OK, {len(problems)} problems")
    for p in problems:
        print("  " + p)
    sys.exit(1 if problems else 0)
