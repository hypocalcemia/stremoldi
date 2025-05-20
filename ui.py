from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

console = Console()

def show_banner():
    ascii_art = r"""
███████╗████████╗██████╗ ███████╗███╗   ███╗ ██████╗ ██╗     ██████╗ ██╗██████╗ ██╗
██╔════╝╚══██╔══╝██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║     ██╔══██╗██║██╔══██╗██║
███████╗   ██║   ██████╔╝█████╗  ██╔████╔██║██║   ██║██║     ██║  ██║██║██████╔╝██║
╚════██║   ██║   ██╔═══╝ ██╔══╝  ██║╚██╔╝██║██║   ██║██║     ██║  ██║██║██╔═══╝ ██║
███████║   ██║   ██║     ███████╗██║ ╚═╝ ██║╚██████╔╝███████╗██████╔╝██║██║     ██║
╚══════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝╚═╝     ╚═╝
"""
    console.print(Panel(ascii_art, title="stremoldi", subtitle="Smart String Analyzer", style="bold cyan"))

def ask_for_file():
    return Prompt.ask("[bold green]Enter path to .exe or binary file[/bold green]")

