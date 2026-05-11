"""Pulsar Display — Clean, minimal, professional.

Design rules:
1. Whitespace > decoration
2. Color only for meaning
3. No walls of symbols
4. Let content breathe
"""

from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from rich.table import Table
from rich.rule import Rule
from rich import box

from pulsar.ui.console import console
from pulsar.ui.themes import (
    FG, FG_MUTED, FG_DIM, FG_FAINT,
    ACCENT, ACCENT_DIM, BLUE, GREEN, YELLOW, RED, ORANGE, CYAN,
    PROMPT_CHAR, ARROW, DOT, CHECK, CROSS, WARN,
    TOOL_ICON, THINK_ICON, BLOCK,
)
from pulsar import __version__


# ═══════════════════════════════════════════════════════════════════
# WELCOME
# ═══════════════════════════════════════════════════════════════════

def show_welcome() -> None:
    """Minimal, clean welcome. No ASCII art wall — just identity."""
    console.print()

    # Brand name — large and clear
    brand = Text()
    brand.append("  pulsar", style=f"bold {ACCENT}")
    brand.append(f"  v{__version__}", style=f"{FG_DIM}")
    console.print(brand)
    console.print()

    # Status line
    status = Text()
    status.append("  model ", style=f"{FG_DIM}")
    status.append("gemini-2.5-flash", style=f"bold {BLUE}")
    status.append(f"  {DOT}  ", style=f"{FG_FAINT}")
    status.append("tools ", style=f"{FG_DIM}")
    status.append("0 loaded", style=f"{FG_MUTED}")
    console.print(status)

    console.print()
    console.print(Rule(style=f"{FG_FAINT}"))
    console.print()


# ═══════════════════════════════════════════════════════════════════
# INPUT
# ═══════════════════════════════════════════════════════════════════

def show_user_message(message: str) -> None:
    """Show what the user typed."""
    text = Text()
    text.append(f"  {PROMPT_CHAR} ", style=f"bold {ACCENT}")
    text.append(message, style=f"{FG}")
    console.print(text)


# ═══════════════════════════════════════════════════════════════════
# RESPONSE
# ═══════════════════════════════════════════════════════════════════

def show_response(content: str) -> None:
    """Render AI response with markdown. Clean, left-aligned."""
    console.print()
    md = Markdown(content, code_theme="monokai")
    console.print(md, width=min(console.width - 4, 96))
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
# TOOL CALLS — the heart of the agent UI
# ═══════════════════════════════════════════════════════════════════

def show_tool_call(tool_name: str, args: dict) -> None:
    """Show a tool being invoked — compact, informative."""
    line = Text()
    line.append(f"  {TOOL_ICON} ", style=f"bold {ORANGE}")
    line.append(tool_name, style=f"bold {ORANGE}")

    if args:
        # Show the most important arg inline
        first_key = next(iter(args))
        first_val = str(args[first_key])
        if len(first_val) > 50:
            first_val = first_val[:47] + "..."
        line.append(f"  {first_val}", style=f"{FG_MUTED}")

    console.print(line)


def show_tool_result(tool_name: str, success: bool = True) -> None:
    """Compact success/fail indicator."""
    line = Text()
    if success:
        line.append(f"  {CHECK} ", style=f"{GREEN}")
        line.append("done", style=f"{FG_DIM}")
    else:
        line.append(f"  {CROSS} ", style=f"{RED}")
        line.append("failed", style=f"{FG_DIM}")
    console.print(line)


def show_tool_output(output: str, max_lines: int = 15) -> None:
    """Show tool output — indented, subtle, truncated."""
    lines = output.split("\n")
    if len(lines) > max_lines:
        display = "\n".join(lines[:max_lines])
        display += f"\n  ... +{len(lines) - max_lines} lines"
    else:
        display = output

    # Indent each line with the block character for visual grouping
    indented_lines = []
    for line in display.split("\n"):
        indented_lines.append(f"  {BLOCK} {line}")
    indented = "\n".join(indented_lines)

    console.print(Text(indented, style=f"{FG_DIM}"))


# ═══════════════════════════════════════════════════════════════════
# PERMISSION
# ═══════════════════════════════════════════════════════════════════

def show_permission_request(action: str, detail: str) -> bool:
    """Ask for approval. Clean, non-scary but clear."""
    console.print()

    line = Text()
    line.append(f"  {WARN} ", style=f"bold {YELLOW}")
    line.append(f"{action}: ", style=f"bold {YELLOW}")
    line.append(detail, style=f"{FG}")
    console.print(line)

    prompt = Text()
    prompt.append("  allow? ", style=f"{FG_MUTED}")
    prompt.append("[y/n] ", style=f"{FG_DIM}")
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
    """Subtle thinking indicator."""
    text = Text()
    text.append(f"  {THINK_ICON} ", style=f"{ACCENT_DIM}")
    text.append(f"{message}...", style=f"italic {ACCENT_DIM}")
    console.print(text)


def show_thinking_content(thought: str) -> None:
    """Show model's internal reasoning — dimmed, indented."""
    lines = thought.strip().split("\n")
    console.print()
    for line in lines:
        text = Text()
        text.append(f"  {BLOCK} ", style=f"{FG_FAINT}")
        text.append(line, style=f"italic {FG_DIM}")
        console.print(text)
    console.print()


# ═══════════════════════════════════════════════════════════════════
# TOKENS
# ═══════════════════════════════════════════════════════════════════

def show_token_usage(
    input_tokens: int, output_tokens: int, model: str = ""
) -> None:
    """Compact token display — right after response."""
    line = Text()
    line.append("  ", style="")
    if model:
        line.append(model, style=f"{FG_DIM}")
        line.append(f"  {DOT}  ", style=f"{FG_FAINT}")
    line.append(f"{input_tokens:,}", style=f"{FG_DIM}")
    line.append(" in ", style=f"{FG_FAINT}")
    line.append(f"{output_tokens:,}", style=f"{FG_DIM}")
    line.append(" out", style=f"{FG_FAINT}")
    console.print(line)


# ═══════════════════════════════════════════════════════════════════
# STATUS MESSAGES
# ═══════════════════════════════════════════════════════════════════

def show_error(title: str, detail: str = "") -> None:
    """Error — red, clear, not panicky."""
    console.print()
    line = Text()
    line.append(f"  {CROSS} ", style=f"bold {RED}")
    line.append(title, style=f"bold {RED}")
    console.print(line)
    if detail:
        console.print(Text(f"    {detail}", style=f"{FG_MUTED}"))
    console.print()


def show_warning(message: str) -> None:
    """Warning — yellow, one line."""
    line = Text()
    line.append(f"  {WARN} ", style=f"bold {YELLOW}")
    line.append(message, style=f"{YELLOW}")
    console.print(line)


def show_success(message: str) -> None:
    """Success — green check, one line."""
    line = Text()
    line.append(f"  {CHECK} ", style=f"{GREEN}")
    line.append(message, style=f"{FG_MUTED}")
    console.print(line)


def show_info(message: str) -> None:
    """Info — subtle, no icon bloat."""
    line = Text()
    line.append(f"  {DOT} ", style=f"{ACCENT_DIM}")
    line.append(message, style=f"{FG_MUTED}")
    console.print(line)


# ═══════════════════════════════════════════════════════════════════
# MISC
# ═══════════════════════════════════════════════════════════════════

def show_separator() -> None:
    """Subtle horizontal divider."""
    console.print(Rule(style=f"{FG_FAINT}"))


def show_goodbye() -> None:
    """Clean exit."""
    console.print()
    line = Text()
    line.append("  goodbye", style=f"italic {FG_DIM}")
    console.print(line)
    console.print()
