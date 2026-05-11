"""Pulsar Spinner — Minimal animated thinking indicator."""

from contextlib import contextmanager
from rich.spinner import Spinner
from rich.live import Live
from rich.text import Text

from pulsar.ui.console import console
from pulsar.ui.themes import ACCENT_DIM, FG_DIM


@contextmanager
def thinking_spinner(message: str = "Thinking"):
    """Show a subtle animated spinner while work happens.

    Usage:
        with thinking_spinner("Reading files"):
            # ... do work ...
            pass
    """
    spinner_text = Text()
    spinner_text.append(f"  {message}...", style=f"italic {ACCENT_DIM}")

    spinner = Spinner("dots", text=spinner_text, style=f"{ACCENT_DIM}")

    with Live(spinner, console=console, refresh_per_second=10, transient=True):
        yield
