"""Pulsar Console — Single Rich console instance for the app."""

from rich.console import Console
from pulsar.ui.themes import PULSAR_THEME

console = Console(theme=PULSAR_THEME, highlight=False)
