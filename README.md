# prgen

Deterministic pull request description generator.

`prgen` reads your local git diff and produces a **structured, correct, boring-by-design** PR title and description.  
No LLM. No GitHub bots. No automation acting on your behalf.

You stay in control.

---

## What it does

- Reads `git diff main...HEAD`
- Classifies the change deterministically (fix / feature / refactor)
- Detects domains (backend / frontend / database)
- Extracts only provable facts
- Generates a complete PR description with:
  - Title
  - Summary
  - Changes
  - Testing
  - Risk / Impact
  - Checklist

If the tool is unsure, it **fails loudly** instead of guessing.

---

## What it does NOT do

- No AI hallucinations
- No auto-posting to GitHub
- No CI bots
- No prompts
- No configuration files
- No background processes

This is a **local developer tool**, not an agent.

---

## Installation

### Recommended (CLI-friendly)
```bash
pipx install git+https://github.com/shaurya-afk/prgen.git@v0.1.1
```

### Alternative (pip)

```bash
pip install git+https://github.com/shaurya-afk/prgen.git@v0.1.1
```

---

## Usage

### Standard flow

```bash
git checkout -b fix-bug
# make code changes
git commit -m "fix: handle null input"
prgen
```

Output is printed to stdout.
Copy and paste it into your GitHub PR description.

---

## Requirements

* Python ≥ 3.10
* Git
* A repository with:

  * At least one commit
  * A base branch (`main`)
  * A feature branch with changes

---

## Error cases (intentional)

`prgen` will refuse to run if:

* Repository has no commits
* You are on the base branch with no diff
* Base branch (`main`) does not exist

Example:

```
No commits found in this repository. Create an initial commit first.
```

This is by design.

---

## Why this exists

Most PR generators:

* Run after PR creation
* Guess intent
* Hallucinate “why”
* Act without permission

`prgen` does the opposite:

* Runs before PR creation
* Uses git as the source of truth
* Never invents information
* Never posts anything automatically

Correctness > cleverness.

---

## Versioning

* Patch (`0.x.1`) → bug fixes, guardrails
* Minor (`0.2.0`) → new deterministic rules
* Major (`1.0.0`) → behavior changes

Determinism is never broken in a minor or patch release.

---

## Roadmap (explicitly optional)

* Optional LLM phrasing layer (schema-validated, off by default)
* GitHub autofill command (`prgen github`)
* Team rule packs

Only if real usage demands it.

---

