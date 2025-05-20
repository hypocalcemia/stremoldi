import typer
from rich.console import Console
from ui import show_banner, ask_for_file
from extractor import extract_strings_from_file
from model import load_model, filter_strings_with_model

app = typer.Typer()
console = Console()

@app.command()
def run():
    show_banner()
    file_path = ask_for_file()

    console.print(f"\n🔍 Extracting strings from [bold yellow]{file_path}[/bold yellow]...\n")
    strings = extract_strings_from_file(file_path)

    console.print(f"🧠 Loading model...\n")
    model, tokenizer = load_model()

    console.print(f"🤖 Analyzing {len(strings)} strings...\n", style="bold blue")
    output = filter_strings_with_model(strings, model, tokenizer)

    console.print("\n🎯 [bold magenta]Interesting strings detected:[/bold magenta]\n")
    console.print(output, style="green")

if __name__ == "__main__":
    app()
