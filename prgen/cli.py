import typer

from prgen.git_reader import read_git_state
from prgen.classifier import classify_change
from prgen.generator import generate_pr_model, render_markdown
from prgen.guards import ensure_valid_state

app = typer.Typer()

@app.command()
def main():
    git_state = read_git_state()
    ensure_valid_state(git_state)

    profile = classify_change(git_state)
    pr_model = generate_pr_model(git_state, profile)
    output = render_markdown(pr_model)

    print(output)

if __name__ == "__main__":
    app()
