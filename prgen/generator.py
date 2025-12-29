from prgen.models import PRModel


def generate_pr_model(git_state: dict, profile: dict) -> PRModel:
    changes = [f"Modified `{f}`" for f in git_state["files"]]

    pr = PRModel(
        title=_title(profile),
        summary=_summary(profile),
        changes=changes,
        testing=_testing(profile),
        risk=_risk(profile),
        checklist=_checklist(profile),
    )

    return pr


def render_markdown(pr: PRModel) -> str:
    return f"""# {pr.title}

## Summary
{pr.summary}

## Changes
{chr(10).join(f"- {c}" for c in pr.changes)}

## Testing
{pr.testing}

## Risk / Impact
{pr.risk}

## Checklist
{chr(10).join(pr.checklist)}
"""


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


def _checklist(profile: dict) -> list[str]:
    items = []

    if profile["has_tests"]:
        items.append("- [x] Tests added or updated")
    else:
        items.append("- [ ] Tests added or updated")

    items.append("- [ ] Docs updated")
    items.append("- [x] No breaking changes")

    return items
