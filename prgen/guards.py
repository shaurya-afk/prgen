def ensure_valid_state(git_state: dict):
    if not git_state["files"]:
        raise RuntimeError(
            "No changes detected. You are likely on the base branch."
        )

    if not git_state["commits"]:
        raise RuntimeError(
            "No commits found on this branch."
        )

    diff_size = len(git_state["diff"].splitlines())
    if diff_size > 2000:
        print("Warning: Large diff detected. Output may be noisy.")
