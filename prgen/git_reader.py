import subprocess

def _run(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode()

import subprocess

def _run(cmd: list[str]) -> str:
    return subprocess.check_output(
        cmd, stderr=subprocess.DEVNULL
    ).decode()

def read_git_state() -> dict:
    # Ensure at least one commit exists
    try:
        _run(["git", "rev-parse", "HEAD"])
    except subprocess.CalledProcessError:
        raise RuntimeError(
            "No commits found in this repository. "
            "Create an initial commit first."
        )

    base = "main"

    try:
        diff = _run(["git", "diff", f"{base}...HEAD"])
        files = _run(
            ["git", "diff", "--name-only", f"{base}...HEAD"]
        ).splitlines()
        commits = _run(
            ["git", "log", "--oneline", f"{base}..HEAD"]
        ).splitlines()
    except subprocess.CalledProcessError:
        raise RuntimeError(
            f"Base branch '{base}' not found. "
            "Ensure you are working from a feature branch."
        )

    return {
        "base": base,
        "files": files,
        "commits": commits,
        "diff": diff,
    }
