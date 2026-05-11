"""Pulsar Console — The single Rich console instance for the entire app.

Every part of Pulsar imports this ONE console. This ensures consistent
theming, no duplicate output, and clean shutdown.
"""

from rich.console import Console
from pulsar.ui.themes import PULSAR_THEME

# The global console — import this everywhere
console = Console(theme=PULSAR_THEME, highlight=False)
