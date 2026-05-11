"""Pulsar Cosmic Theme — The color system that makes Pulsar feel alive.

Design: Deep space aesthetic — nebula purples, electric cyans, warm star golds.
Enhanced with clean spacing and professional typography from modern terminal agents.
"""

from rich.theme import Theme
from rich.style import Style

# ─── Core Palette ───────────────────────────────────────────────────
# Handpicked for dark terminals. Think deep space.

VOID = "#0a0a0f"           # Deep space black
NEBULA = "#c792ea"         # Soft purple (brand)
NEBULA_DIM = "#7c4dab"     # Muted purple
PLASMA = "#82aaff"         # Electric blue (info)
CYAN_GLOW = "#89ddff"      # Bright cyan (interactive)
STAR_GOLD = "#ffcb6b"      # Warm gold (warnings)
NOVA_RED = "#ff5370"        # Alert red (errors)
SOLAR_GREEN = "#c3e88d"    # Lime green (success)
COMET_ORANGE = "#f78c6c"   # Warm orange (tool calls)
DUST = "#676e95"           # Cool gray (muted)
STARDUST = "#a6accd"       # Light gray (secondary text)
WHITE_HOT = "#eeffff"      # Near-white (primary text)
DEEP_GRAY = "#3b3f5c"      # Very subtle borders

# ─── Semantic Styles ────────────────────────────────────────────────

PULSAR_THEME = Theme({
    # Text hierarchy
    "primary": Style(color=WHITE_HOT),
    "secondary": Style(color=STARDUST),
    "muted": Style(color=DUST),
    "dim": Style(color=DEEP_GRAY),

    # Brand
    "accent": Style(color=NEBULA, bold=True),
    "accent.dim": Style(color=NEBULA_DIM),
    "brand": Style(color=NEBULA, bold=True),

    # Semantic
    "info": Style(color=PLASMA),
    "success": Style(color=SOLAR_GREEN),
    "warning": Style(color=STAR_GOLD),
    "error": Style(color=NOVA_RED, bold=True),

    # UI Elements
    "prompt": Style(color=CYAN_GLOW, bold=True),
    "prompt.arrow": Style(color=NEBULA, bold=True),
    "border": Style(color=DEEP_GRAY),
    "border.accent": Style(color=NEBULA_DIM),
    "header": Style(color=WHITE_HOT, bold=True),

    # Agent-specific
    "tool.name": Style(color=COMET_ORANGE, bold=True),
    "tool.arg": Style(color=STARDUST),
    "tool.result": Style(color=SOLAR_GREEN),
    "tool.error": Style(color=NOVA_RED),
    "thinking": Style(color=NEBULA_DIM, italic=True),
    "model": Style(color=PLASMA, bold=True),
    "tokens": Style(color=DUST),
    "cost": Style(color=STAR_GOLD),

    # Code
    "code": Style(color=CYAN_GLOW),
    "filename": Style(color=PLASMA, underline=True),
})

# ─── Icons ───────────────────────────────────────────────────────────

ARROW_RIGHT = "→"
CHEVRON = "›"
DIAMOND = "◆"
STAR = "✦"
SPARK = "⚡"
GEAR = "⚙"
CHECK = "✓"
CROSS = "✗"
WARNING_ICON = "⚠"
DOT = "·"
BLOCK = "│"
TOOL_ARROW = "▸"
CIRCLE_DOT = "◌"
