"""Pulsar Display — Cosmic visual system, enhanced.

Original Pulsar aesthetic (banner, panels, cosmic icons) upgraded with:
- Cleaner tool call grouping with │ block lines
- Better thinking display
- Compact but rich token display
- Improved spacing and breathing room
"""

from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from rich.table import Table
from rich.rule import Rule
from rich import box

from pulsar.ui.console import console
from pulsar.ui.themes import (
    NEBULA, NEBULA_DIM, PLASMA, CYAN_GLOW, STAR_GOLD, NOVA_RED,
    SOLAR_GREEN, COMET_ORANGE, DUST, STARDUST, WHITE_HOT, DEEP_GRAY,
    ARROW_RIGHT, CHEVRON, DIAMOND, STAR, SPARK, GEAR, CHECK, CROSS,
    WARNING_ICON, DOT, BLOCK, TOOL_ARROW, CIRCLE_DOT,
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
    tagline = Text(justify="center")
    tagline.append(f" {STAR} ", style=f"bold {NEBULA}")
    tagline.append("Multi-Provider AI Coding Agent", style=f"bold {WHITE_HOT}")
    tagline.append(f" {STAR}", style=f"bold {NEBULA}")
    console.print(tagline)
    console.print()

    # Status bar — compact info strip
    info = Text(justify="center")
    info.append(f" {DIAMOND} ", style=f"{STARDUST}")
    info.append(f"v{__version__}", style=f"{STARDUST}")
    info.append(f"   {SPARK} ", style=f"{PLASMA}")
    info.append("gemini-2.5-flash", style=f"bold {PLASMA}")
    info.append(f"   {GEAR} ", style=f"{DUST}")
    info.append("0 tools", style=f"{DUST}")
    console.print(info)

    console.print()
    console.print(Rule(style=f"{DEEP_GRAY}"))
    console.print()

    # Hints
    hints = Text(justify="center")
    hints.append("Type a message to start", style=f"{STARDUST}")
    hints.append(f"  {DOT}  ", style=f"{DEEP_GRAY}")
    hints.append("/help", style=f"bold {CYAN_GLOW}")
    hints.append(" for commands", style=f"{STARDUST}")
    hints.append(f"  {DOT}  ", style=f"{DEEP_GRAY}")
    hints.append("Ctrl+C", style=f"bold {STAR_GOLD}")
    hints.append(" to exit", style=f"{STARDUST}")
    console.print(hints)
    console.print()


# ═══════════════════════════════════════════════════════════════════
# INPUT
# ═══════════════════════════════════════════════════════════════════

def show_user_message(message: str) -> None:
    """Display what the user typed."""
    text = Text()
    text.append(f" {CHEVRON} ", style=f"bold {NEBULA}")
    text.append(message, style=f"{WHITE_HOT}")
    console.print(text)


# ═══════════════════════════════════════════════════════════════════
# RESPONSES
# ═══════════════════════════════════════════════════════════════════

def show_response(content: str) -> None:
    """Render AI response — markdown with syntax highlighting."""
    console.print()
    md = Markdown(content, code_theme="one-dark")
    console.print(md, width=min(console.width - 2, 96))
    console.print()


def show_streaming_chunk(text: str) -> None:
    """Print a streaming chunk inline."""
    console.print(text, end="", highlight=False)


def show_streaming_start() -> None:
    """Mark start of streaming."""
    console.print()


def show_streaming_end() -> None:
    """Mark end of streaming."""
    console.print()
    console.print()


# ═══════════════════════════════════════════════════════════════════
# TOOL CALLS — grouped with block lines
# ═══════════════════════════════════════════════════════════════════

def show_tool_call(tool_name: str, args: dict) -> None:
    """Show a tool being invoked — icon + name + key arg."""
    line = Text()
    line.append(f"  {TOOL_ARROW} ", style=f"bold {COMET_ORANGE}")
    line.append(tool_name, style=f"bold {COMET_ORANGE}")

    if args:
        first_key = next(iter(args))
        first_val = str(args[first_key])
        if len(first_val) > 55:
            first_val = first_val[:52] + "..."
        line.append(f"  {ARROW_RIGHT} ", style=f"{DUST}")
        line.append(first_val, style=f"{STARDUST}")

    console.print(line)


def show_tool_result(tool_name: str, success: bool = True) -> None:
    """Compact tool completion status."""
    line = Text()
    if success:
        line.append(f"  {CHECK} ", style=f"bold {SOLAR_GREEN}")
        line.append(f"{tool_name} completed", style=f"{DUST}")
    else:
        line.append(f"  {CROSS} ", style=f"bold {NOVA_RED}")
        line.append(f"{tool_name} failed", style=f"{DUST}")
    console.print(line)


def show_tool_output(output: str, max_lines: int = 20) -> None:
    """Show tool output — indented with block character for grouping."""
    lines = output.split("\n")
    if len(lines) > max_lines:
        display_lines = lines[:max_lines]
        display_lines.append(f"... +{len(lines) - max_lines} more lines")
    else:
        display_lines = lines

    for line in display_lines:
        text = Text()
        text.append(f"  {BLOCK} ", style=f"{DEEP_GRAY}")
        text.append(line, style=f"{STARDUST}")
        console.print(text)


# ═══════════════════════════════════════════════════════════════════
# PERMISSION — panel style (clear, intentional)
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
# THINKING
# ═══════════════════════════════════════════════════════════════════

def show_thinking(message: str = "Thinking") -> None:
    """Thinking indicator with cosmic icon."""
    text = Text()
    text.append(f"  {CIRCLE_DOT} ", style=f"bold {NEBULA_DIM}")
    text.append(f"{message}...", style=f"italic {NEBULA_DIM}")
    console.print(text)


def show_thinking_content(thought: str) -> None:
    """Show model reasoning — indented with block lines, dimmed italic."""
    lines = thought.strip().split("\n")
    console.print()
    for line in lines:
        text = Text()
        text.append(f"  {BLOCK} ", style=f"{NEBULA_DIM}")
        text.append(line, style=f"italic {DUST}")
        console.print(text)
    console.print()


# ═══════════════════════════════════════════════════════════════════
# TOKEN USAGE
# ═══════════════════════════════════════════════════════════════════

def show_token_usage(
    input_tokens: int, output_tokens: int, model: str = ""
) -> None:
    """Token usage — compact single line with model name."""
    line = Text()
    line.append("  ", style="")
    if model:
        line.append(f"{SPARK} ", style=f"{PLASMA}")
        line.append(model, style=f"{PLASMA}")
        line.append(f"  {DOT}  ", style=f"{DEEP_GRAY}")
    line.append(f"{input_tokens:,} in", style=f"{DUST}")
    line.append(f"  {DOT}  ", style=f"{DEEP_GRAY}")
    line.append(f"{output_tokens:,} out", style=f"{DUST}")
    console.print(line)


# ═══════════════════════════════════════════════════════════════════
# STATUS MESSAGES
# ═══════════════════════════════════════════════════════════════════

def show_error(title: str, detail: str = "") -> None:
    """Error — red panel, clear and intentional."""
    console.print()
    if detail:
        panel = Panel(
            Text(detail, style=f"{WHITE_HOT}"),
            title=Text(f" {CROSS}  {title} ", style=f"bold {NOVA_RED}"),
            border_style=f"{NOVA_RED}",
            box=box.ROUNDED,
            padding=(0, 1),
        )
        console.print(panel)
    else:
        line = Text()
        line.append(f"  {CROSS} ", style=f"bold {NOVA_RED}")
        line.append(title, style=f"bold {NOVA_RED}")
        console.print(line)
    console.print()


def show_warning(message: str) -> None:
    """Warning — gold, one line."""
    line = Text()
    line.append(f"  {WARNING_ICON}  ", style=f"bold {STAR_GOLD}")
    line.append(message, style=f"{STAR_GOLD}")
    console.print(line)


def show_success(message: str) -> None:
    """Success — green check."""
    line = Text()
    line.append(f"  {CHECK} ", style=f"bold {SOLAR_GREEN}")
    line.append(message, style=f"{SOLAR_GREEN}")
    console.print(line)


def show_info(message: str) -> None:
    """Info — diamond + subtle text."""
    line = Text()
    line.append(f"  {DIAMOND} ", style=f"bold {PLASMA}")
    line.append(message, style=f"{STARDUST}")
    console.print(line)


# ═══════════════════════════════════════════════════════════════════
# MISC
# ═══════════════════════════════════════════════════════════════════

def show_separator() -> None:
    """Subtle cosmic divider."""
    console.print(Rule(style=f"{DEEP_GRAY}"))


def show_goodbye() -> None:
    """Cosmic goodbye."""
    console.print()
    text = Text()
    text.append(f"  {STAR} ", style=f"bold {NEBULA}")
    text.append("See you next time, pilot.", style=f"italic {STARDUST}")
    text.append(f" {STAR}", style=f"bold {NEBULA}")
    console.print(text)
    console.print()
