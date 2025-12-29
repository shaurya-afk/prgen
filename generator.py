def generate_pr(git_state: dict, profile: dict) -> str:
    title = _title(profile)
    body = [
        f"## Summary\n{_summary(profile)}",
        f"## Changes\n{_changes(git_state)}",
        f"## Testing\n{_testing(profile)}",
        f"## Risk / Impact\n{_risk(profile)}",
        f"## Checklist\n{_checklist(profile)}",
    ]
    return f"# {title}\n\n" + "\n\n".join(body)

def _title(profile):
    return f"{profile['type'].capitalize()} changes in {', '.join(profile['domains']) or 'codebase'}"

def _summary(profile):
    return f"This PR introduces {profile['type']} changes affecting the {', '.join(profile['domains']) or 'codebase'}."

def _changes(git_state):
    return "\n".join(f"- Modified `{f}`" for f in git_state["files"])

def _testing(profile):
    return "- Tests updated" if profile["has_tests"] else "- Not applicable"

def _risk(profile):
    if "database" in profile["domains"]:
        return "Medium risk due to database changes."
    return "Low risk."

def _checklist(profile):
    return "\n".join([
        "- [x] Tests added or updated" if profile["has_tests"] else "- [ ] Tests added or updated",
        "- [ ] Docs updated",
        "- [x] No breaking changes",
    ])
