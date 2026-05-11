"""Pulsar Console — Single Rich console instance."""

from rich.console import Console
from pulsar.ui.themes import PULSAR_THEME

console = Console(theme=PULSAR_THEME, highlight=False)
