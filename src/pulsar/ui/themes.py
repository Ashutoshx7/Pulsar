"""Pulsar Theme — Clean, professional, minimal.

Design philosophy: Claude Code meets Vercel.
- Restrained color use — most text is white/gray
- Color only for SEMANTIC meaning (success, error, accent)
- Plenty of whitespace
- Thin, subtle borders
- Typography does the heavy lifting
"""

from rich.theme import Theme
from rich.style import Style

# ─── Core Palette ───────────────────────────────────────────────────
# Inspired by Vercel/Linear dark mode — clean, not flashy.

BG = "#0a0a0a"              # True dark
FG = "#ededed"              # Primary text — bright but not blinding
FG_MUTED = "#888888"        # Secondary text
FG_DIM = "#555555"          # Tertiary / borders
FG_FAINT = "#333333"        # Very subtle separators

ACCENT = "#a78bfa"          # Violet — primary brand accent
ACCENT_DIM = "#7c6aad"     # Muted violet
BLUE = "#60a5fa"            # Links, model names
CYAN = "#67e8f9"            # Highlights, interactive
GREEN = "#4ade80"           # Success
YELLOW = "#fbbf24"          # Warnings
RED = "#f87171"             # Errors
ORANGE = "#fb923c"          # Tool calls

# ─── Theme ──────────────────────────────────────────────────────────

PULSAR_THEME = Theme({
    # Text hierarchy
    "primary": Style(color=FG),
    "secondary": Style(color=FG_MUTED),
    "muted": Style(color=FG_DIM),
    "dim": Style(color=FG_FAINT),

    # Brand
    "accent": Style(color=ACCENT),
    "accent.bold": Style(color=ACCENT, bold=True),
    "accent.dim": Style(color=ACCENT_DIM),

    # Semantic
    "info": Style(color=BLUE),
    "success": Style(color=GREEN),
    "warning": Style(color=YELLOW),
    "error": Style(color=RED, bold=True),

    # UI
    "prompt": Style(color=ACCENT, bold=True),
    "border": Style(color=FG_DIM),
    "border.subtle": Style(color=FG_FAINT),
    "header": Style(color=FG, bold=True),

    # Agent
    "tool.name": Style(color=ORANGE, bold=True),
    "tool.arg": Style(color=FG_MUTED),
    "thinking": Style(color=ACCENT_DIM, italic=True),
    "model": Style(color=BLUE),
    "tokens": Style(color=FG_DIM),
    "cost": Style(color=YELLOW),

    # Code
    "code": Style(color=CYAN),
    "filename": Style(color=BLUE, underline=True),
})

# ─── Icons (minimal, tasteful) ──────────────────────────────────────

PROMPT_CHAR = "❯"
ARROW = "→"
DOT = "·"
CHECK = "✓"
CROSS = "✕"
WARN = "!"
TOOL_ICON = "▸"
THINK_ICON = "◌"
BLOCK = "│"
