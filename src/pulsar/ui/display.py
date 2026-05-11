"""Pulsar Display — All the visual components that make Pulsar look premium.

This module renders everything the user sees: welcome screen, responses,
tool calls, errors, thinking indicators, and more.
"""

from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.columns import Columns
from rich.table import Table
from rich.rule import Rule
from rich import box

from pulsar.ui.console import console
from pulsar.ui.themes import (
    NEBULA, CYAN_GLOW, DUST, STARDUST, COMET_ORANGE, SOLAR_GREEN,
    NOVA_RED, STAR_GOLD, PLASMA, WHITE_HOT, NEBULA_DIM,
    ARROW_RIGHT, CHEVRON, DIAMOND, GEAR, CHECK, CROSS,
    WARNING_ICON, STAR, SPARK, DOT,
)
from pulsar import __version__


# ═══════════════════════════════════════════════════════════════════
# WELCOME SCREEN
# ═══════════════════════════════════════════════════════════════════

BANNER = r"""
[bold #c792ea] ██████╗ ██╗   ██╗██╗     ███████╗ █████╗ ██████╗[/]
[bold #c792ea] ██╔══██╗██║   ██║██║     ██╔════╝██╔══██╗██╔══██╗[/]
[bold #89ddff] ██████╔╝██║   ██║██║     ███████╗███████║██████╔╝[/]
[bold #89ddff] ██╔═══╝ ██║   ██║██║     ╚════██║██╔══██║██╔══██╗[/]
[bold #82aaff] ██║     ╚██████╔╝███████╗███████║██║  ██║██║  ██║[/]
[bold #82aaff] ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝[/]"""


def show_welcome() -> None:
    """Display the cosmic welcome screen."""
    console.print()
    console.print(BANNER)
    console.print()

    # Tagline
    tagline = Text()
    tagline.append(f"  {STAR} ", style=f"bold {NEBULA}")
    tagline.append("Multi-Provider AI Coding Agent", style=f"bold {WHITE_HOT}")
    tagline.append(f"  {STAR}", style=f"bold {NEBULA}")
    console.print(tagline)
    console.print()

    # Info bar
    info = Table.grid(padding=(0, 3))
    info.add_row(
        Text(f"{DIAMOND} v{__version__}", style=f"{STARDUST}"),
        Text(f"{SPARK} gemini-2.5-flash", style=f"bold {PLASMA}"),
        Text(f"{GEAR} 0 tools loaded", style=f"{DUST}"),
    )
    console.print(info, justify="center")

    # Separator
    console.print()
    console.print(Rule(style=f"{DUST}"))
    console.print()

    # Quick hints
    hints = Text()
    hints.append("  Type a message to start", style=f"{STARDUST}")
    hints.append("  │  ", style=f"{DUST}")
    hints.append("/help", style=f"bold {CYAN_GLOW}")
    hints.append(" for commands", style=f"{STARDUST}")
    hints.append("  │  ", style=f"{DUST}")
    hints.append("Ctrl+C", style=f"bold {STAR_GOLD}")
    hints.append(" to exit", style=f"{STARDUST}")
    console.print(hints)
    console.print()


# ═══════════════════════════════════════════════════════════════════
# INPUT PROMPT
# ═══════════════════════════════════════════════════════════════════

def get_input_prompt() -> Text:
    """Return the styled input prompt text."""
    prompt = Text()
    prompt.append(f" {CHEVRON} ", style=f"bold {NEBULA}")
    return prompt


def show_user_message(message: str) -> None:
    """Display what the user typed (for history/logging)."""
    text = Text()
    text.append(f" {CHEVRON} ", style=f"bold {NEBULA}")
    text.append(message, style=f"{WHITE_HOT}")
    console.print(text)


# ═══════════════════════════════════════════════════════════════════
# RESPONSE RENDERING
# ═══════════════════════════════════════════════════════════════════

def show_response(content: str) -> None:
    """Render an AI response with markdown formatting."""
    console.print()
    md = Markdown(content, code_theme="one-dark")
    console.print(md, width=min(console.width, 100))
    console.print()


def show_streaming_chunk(text: str) -> None:
    """Print a single streaming chunk (no newline)."""
    console.print(text, end="", highlight=False)


def show_streaming_start() -> None:
    """Visual indicator that streaming has begun."""
    console.print()


def show_streaming_end() -> None:
    """Visual indicator that streaming is complete."""
    console.print()
    console.print()


# ═══════════════════════════════════════════════════════════════════
# TOOL CALL DISPLAY
# ═══════════════════════════════════════════════════════════════════

def show_tool_call(tool_name: str, args: dict) -> None:
    """Show that a tool is being called — the 'agent is working' indicator."""
    header = Text()
    header.append(f"  {GEAR} ", style=f"bold {COMET_ORANGE}")
    header.append(tool_name, style=f"bold {COMET_ORANGE}")

    # Show key arguments inline
    if args:
        header.append("  ", style="")
        arg_parts = []
        for key, value in args.items():
            val_str = str(value)
            if len(val_str) > 60:
                val_str = val_str[:57] + "..."
            arg_parts.append(f"{key}={val_str}")
        header.append(ARROW_RIGHT + " ", style=f"{DUST}")
        header.append(", ".join(arg_parts), style=f"{STARDUST}")

    console.print(header)


def show_tool_result(tool_name: str, success: bool = True) -> None:
    """Show tool completion status."""
    status = Text()
    if success:
        status.append(f"  {CHECK} ", style=f"bold {SOLAR_GREEN}")
        status.append(f"{tool_name} completed", style=f"{STARDUST}")
    else:
        status.append(f"  {CROSS} ", style=f"bold {NOVA_RED}")
        status.append(f"{tool_name} failed", style=f"{STARDUST}")
    console.print(status)


def show_tool_output(output: str, max_lines: int = 20) -> None:
    """Show truncated tool output in a subtle panel."""
    lines = output.split("\n")
    if len(lines) > max_lines:
        truncated = "\n".join(lines[:max_lines])
        truncated += f"\n... ({len(lines) - max_lines} more lines)"
    else:
        truncated = output

    panel = Panel(
        Text(truncated, style=f"{STARDUST}"),
        border_style=f"{DUST}",
        box=box.ROUNDED,
        padding=(0, 1),
        expand=False,
    )
    console.print(panel)


# ═══════════════════════════════════════════════════════════════════
# PERMISSION PROMPT
# ═══════════════════════════════════════════════════════════════════

def show_permission_request(action: str, detail: str) -> bool:
    """Ask user to approve a dangerous action. Returns True if approved."""
    console.print()
    panel = Panel(
        Text(detail, style=f"{WHITE_HOT}"),
        title=Text(f" {WARNING_ICON}  {action} ", style=f"bold {STAR_GOLD}"),
        border_style=f"{STAR_GOLD}",
        box=box.ROUNDED,
        padding=(0, 1),
    )
    console.print(panel)

    prompt = Text()
    prompt.append(f"  Allow? ", style=f"bold {STAR_GOLD}")
    prompt.append("[y/n] ", style=f"{DUST}")
    console.print(prompt, end="")

    try:
        response = input().strip().lower()
        return response in ("y", "yes")
    except (EOFError, KeyboardInterrupt):
        console.print()
        return False


# ═══════════════════════════════════════════════════════════════════
# THINKING / STATUS
# ═══════════════════════════════════════════════════════════════════

def show_thinking(message: str = "Thinking") -> None:
    """Show a thinking/processing indicator."""
    text = Text()
    text.append(f"  {DOT} ", style=f"bold {NEBULA_DIM}")
    text.append(message, style=f"italic {NEBULA_DIM}")
    text.append("...", style=f"italic {DUST}")
    console.print(text)


def show_thinking_content(thought: str) -> None:
    """Display the model's thinking/reasoning in a dimmed panel."""
    panel = Panel(
        Text(thought, style=f"italic {DUST}"),
        title=Text(" 💭 Thinking ", style=f"italic {NEBULA_DIM}"),
        border_style=f"{NEBULA_DIM}",
        box=box.ROUNDED,
        padding=(0, 1),
        expand=False,
    )
    console.print(panel)


# ═══════════════════════════════════════════════════════════════════
# TOKEN USAGE
# ═══════════════════════════════════════════════════════════════════

def show_token_usage(input_tokens: int, output_tokens: int, model: str = "") -> None:
    """Display token usage after each response."""
    usage = Text()
    usage.append(f"  {DOT} ", style=f"{DUST}")
    if model:
        usage.append(f"{model}", style=f"{PLASMA}")
        usage.append("  │  ", style=f"{DUST}")
    usage.append(f"{input_tokens:,} in", style=f"{DUST}")
    usage.append(" / ", style=f"{DUST}")
    usage.append(f"{output_tokens:,} out", style=f"{DUST}")
    console.print(usage)


# ═══════════════════════════════════════════════════════════════════
# ERRORS & WARNINGS
# ═══════════════════════════════════════════════════════════════════

def show_error(title: str, detail: str = "") -> None:
    """Display an error message in a red panel."""
    content = Text(detail, style=f"{WHITE_HOT}") if detail else Text(title, style=f"{WHITE_HOT}")
    panel = Panel(
        content,
        title=Text(f" {CROSS}  {title} ", style=f"bold {NOVA_RED}"),
        border_style=f"{NOVA_RED}",
        box=box.ROUNDED,
        padding=(0, 1),
    )
    console.print()
    console.print(panel)
    console.print()


def show_warning(message: str) -> None:
    """Display a warning message."""
    text = Text()
    text.append(f"  {WARNING_ICON}  ", style=f"bold {STAR_GOLD}")
    text.append(message, style=f"{STAR_GOLD}")
    console.print(text)


def show_success(message: str) -> None:
    """Display a success message."""
    text = Text()
    text.append(f"  {CHECK} ", style=f"bold {SOLAR_GREEN}")
    text.append(message, style=f"{SOLAR_GREEN}")
    console.print(text)


def show_info(message: str) -> None:
    """Display an info message."""
    text = Text()
    text.append(f"  {DIAMOND} ", style=f"bold {PLASMA}")
    text.append(message, style=f"{STARDUST}")
    console.print(text)


# ═══════════════════════════════════════════════════════════════════
# SEPARATOR & MISC
# ═══════════════════════════════════════════════════════════════════

def show_separator() -> None:
    """Draw a subtle horizontal rule."""
    console.print(Rule(style=f"{DUST}"))


def show_goodbye() -> None:
    """Show exit message."""
    console.print()
    text = Text()
    text.append(f"  {STAR} ", style=f"bold {NEBULA}")
    text.append("See you next time, pilot.", style=f"italic {STARDUST}")
    text.append(f" {STAR}", style=f"bold {NEBULA}")
    console.print(text)
    console.print()
