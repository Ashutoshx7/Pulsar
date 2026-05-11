"""Pulsar Spinner — Animated thinking indicator using Rich."""

from contextlib import contextmanager
from rich.spinner import Spinner
from rich.live import Live
from rich.text import Text

from pulsar.ui.console import console
from pulsar.ui.themes import NEBULA_DIM, DUST


@contextmanager
def thinking_spinner(message: str = "Thinking"):
    """Context manager that shows an animated spinner while work is happening.

    Usage:
        with thinking_spinner("Reading files"):
            # ... do work ...
            pass
    """
    spinner_text = Text()
    spinner_text.append(f"  {message}", style=f"italic {NEBULA_DIM}")
    spinner_text.append("...", style=f"italic {DUST}")

    spinner = Spinner("dots", text=spinner_text, style=f"bold {NEBULA_DIM}")

    with Live(spinner, console=console, refresh_per_second=12, transient=True):
        yield
