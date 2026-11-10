"""Alpha2-Roger system report v0.1: one command that captures everything Claudia needs to diagnose a problem.

Run from anywhere:  python3 tools/system_report.py
It writes diagnostics/system_report_<timestamp>.md and prints the path.  Send or paste that file to Claudia.
The diagnostics/ folder is git-ignored, so reports never land in the public repo.

What it captures:
  - Git: branch, latest commit, sync with GitHub, uncommitted changes, recent history
  - Versions: the full version check (missing versions, VERSIONS.md mismatches)
  - Environment: OS, Python and package versions, Godot and Claude Code if installed
  - Project: STATUS.md, repo file counts, the Godot project if it exists, data files that fail to load
"""
__version__ = "0.1"

import datetime, importlib, json, platform, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import version_check  # noqa: E402


def run(cmd):
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=30)
        return (r.stdout or r.stderr).rstrip() or "(no output)"
    except Exception as e:
        return f"(could not run: {e})"


def block(text):
    return "```\n" + text + "\n```\n"


def main():
    now = datetime.datetime.now()
    lines = [f"# Alpha2-Roger system report", "", f"**Report v{__version__}, generated {now:%Y-%m-%d %H:%M:%S}**", ""]

    lines += ["## Git", ""]
    fetched = run(["git", "fetch", "-q", "origin", "main"])
    sync = run(["git", "rev-list", "--left-right", "--count", "FETCH_HEAD...HEAD"])
    if len(sync.split()) == 2 and all(x.isdigit() for x in sync.split()):
        sync = "behind {}, ahead {}".format(*sync.split())
    if fetched != "(no output)":
        sync = f"could not reach GitHub: {fetched.splitlines()[-1]}"
    lines += [f"- Branch: `{run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])}`",
              f"- Latest commit: `{run(['git', 'log', '-1', '--format=%h %ad %s', '--date=short'])}`",
              f"- Behind/ahead of GitHub main: `{sync}`", ""]
    lines += ["Uncommitted changes:", block(run(["git", "status", "--short"]))]
    lines += ["Recent history:", block(run(["git", "log", "-10", "--format=%h %ad %an  %s", "--date=short"]))]

    lines += ["## Versions", ""]
    ok, problems = version_check.check()
    lines += [f"- {ok} files OK, {len(problems)} problems", ""]
    lines += [block("\n".join(problems) if problems else "All versions match.")]

    lines += ["## Environment", ""]
    lines += [f"- OS: {platform.platform()}", f"- Python: {sys.version.split()[0]}"]
    for pkg in ("numpy", "PIL", "scipy"):
        try:
            m = importlib.import_module(pkg)
            lines.append(f"- {pkg}: {getattr(m, '__version__', 'installed')}")
        except Exception:
            lines.append(f"- {pkg}: not installed")
    for tool, args in (("godot", ["--version"]), ("godot4", ["--version"]), ("claude", ["--version"]), ("git", ["--version"])):
        path = shutil.which(tool)
        lines.append(f"- {tool}: {run([path] + args) if path else 'not found'}")
    lines.append("")

    lines += ["## Project", ""]
    files = [f for f in run(["git", "ls-files"]).splitlines() if f]
    lines.append(f"- Tracked files: {len(files)}")
    game = ROOT / "game" / "project.godot"
    lines.append(f"- Godot project: {'present' if game.exists() else 'not created yet'}")
    bad = []
    for jf in (ROOT / "tools" / "data").glob("*.json"):
        try:
            json.loads(jf.read_text())
        except Exception as e:
            bad.append(f"{jf.relative_to(ROOT)}: {e}")
    lines.append(f"- Data files that fail to load: {len(bad)}")
    lines += [f"  - {b}" for b in bad]
    lines.append("")
    status = ROOT / "STATUS.md"
    lines += ["## STATUS.md", "", status.read_text() if status.exists() else "(missing)"]

    outdir = ROOT / "diagnostics"
    outdir.mkdir(exist_ok=True)
    out = outdir / f"system_report_{now:%Y%m%d_%H%M%S}.md"
    out.write_text("\n".join(lines))
    print(f"System report written: {out}")
    print(f"Versions: {ok} OK, {len(problems)} problems")


if __name__ == "__main__":
    main()
