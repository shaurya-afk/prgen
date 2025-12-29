import typer
from prgen.git_reader import read_git_state
from prgen.classifier import classify_change
from prgen.generator import generate_pr

app = typer.Typer()

@app.command()
def main():
    git_state = read_git_state()
    profile = classify_change(git_state)
    pr_md = generate_pr(git_state, profile)
    print(pr_md)

if __name__ == "__main__":
    app()
