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

    change_type = "refactor"
    for c in git_state["commits"]:
        if c.startswith("fix"):
            change_type = "fix"
        elif c.startswith("feat"):
            change_type = "feature"

    return {
        "type": change_type,
        "domains": sorted(domains),
        "has_tests": has_tests,
    }
