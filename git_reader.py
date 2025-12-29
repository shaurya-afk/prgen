import subprocess

def _run(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode()

def read_git_state() -> dict:
    base = "main"

    diff = _run(["git", "diff", f"{base}...HEAD"])
    files = _run(["git", "diff", "--name-only", f"{base}...HEAD"]).splitlines()
    commits = _run(["git", "log", "--oneline", f"{base}..HEAD"]).splitlines()

    return {
        "base": base,
        "files": files,
        "commits": commits,
        "diff": diff,
    }
