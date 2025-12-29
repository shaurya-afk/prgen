def _normalize_commit(msg: str) -> str:
    msg = msg.lower().strip()

    replacements = {
        "fixed": "fix",
        "fixes": "fix",
        "added": "feat",
        "adds": "feat",
        "adding": "feat",
    }

    for k, v in replacements.items():
        if msg.startswith(k):
            return v + msg[len(k):]

    return msg


def classify_change(git_state: dict) -> dict:
    files = git_state["files"]

    domains = set()
    has_tests = False

    for f in files:
        if f.endswith((".ts", ".tsx", ".js", ".jsx")):
            domains.add("frontend")
        if f.endswith(".py"):
            domains.add("backend")
        if "migration" in f or f.endswith(".sql"):
            domains.add("database")
        if "test" in f.lower():
            has_tests = True

    normalized_commits = [_normalize_commit(c) for c in git_state["commits"]]

    change_type = "refactor"
    for c in normalized_commits:
        if c.startswith("fix"):
            change_type = "fix"
            break
        elif c.startswith("feat"):
            change_type = "feature"
            break

    return {
        "type": change_type,
        "domains": sorted(domains),
        "has_tests": has_tests,
    }
