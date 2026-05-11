"""Pulsar Cosmic Theme — The color system that makes Pulsar feel alive.

Every color is handpicked for a dark terminal. Think deep space:
nebula purples, electric cyans, warm star golds, and cold void grays.
"""

from rich.theme import Theme
from rich.style import Style

# ─── Core Palette ───────────────────────────────────────────────────
# These are the raw hex colors. Everything else references these.

VOID = "#0a0a0f"           # Deep space black (backgrounds)
NEBULA = "#c792ea"         # Soft purple (primary accent)
NEBULA_DIM = "#7c4dab"     # Muted purple (secondary)
PLASMA = "#82aaff"         # Electric blue (info, links)
CYAN_GLOW = "#89ddff"      # Bright cyan (highlights)
STAR_GOLD = "#ffcb6b"      # Warm gold (warnings, emphasis)
NOVA_RED = "#ff5370"        # Alert red (errors, danger)
SOLAR_GREEN = "#c3e88d"    # Lime green (success, approved)
COMET_ORANGE = "#f78c6c"   # Warm orange (tool calls)
DUST = "#676e95"           # Cool gray (muted text, borders)
STARDUST = "#a6accd"       # Light gray (secondary text)
WHITE_HOT = "#eeffff"      # Near-white (primary text)

# ─── Semantic Styles ────────────────────────────────────────────────

PULSAR_THEME = Theme({
    # Text hierarchy
    "primary": Style(color=WHITE_HOT),
    "secondary": Style(color=STARDUST),
    "muted": Style(color=DUST),
    "dim": Style(color=DUST, dim=True),

    # Brand
    "accent": Style(color=NEBULA, bold=True),
    "accent.dim": Style(color=NEBULA_DIM),
    "brand": Style(color=NEBULA, bold=True),

    # Semantic
    "info": Style(color=PLASMA),
    "success": Style(color=SOLAR_GREEN),
    "warning": Style(color=STAR_GOLD),
    "error": Style(color=NOVA_RED, bold=True),
    "danger": Style(color=NOVA_RED),

    # UI Elements
    "prompt": Style(color=CYAN_GLOW, bold=True),
    "prompt.arrow": Style(color=NEBULA, bold=True),
    "border": Style(color=DUST),
    "border.accent": Style(color=NEBULA_DIM),
    "header": Style(color=WHITE_HOT, bold=True),
    "subheader": Style(color=STARDUST, italic=True),

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
    "code.inline": Style(color=SOLAR_GREEN),
    "filename": Style(color=PLASMA, underline=True),
    "line_number": Style(color=DUST),
})

# ─── Box Characters ─────────────────────────────────────────────────
# For custom borders and separators

HORIZONTAL_LINE = "─"
VERTICAL_LINE = "│"
TOP_LEFT = "╭"
TOP_RIGHT = "╮"
BOTTOM_LEFT = "╰"
BOTTOM_RIGHT = "╯"
DOT = "•"
ARROW_RIGHT = "→"
CHEVRON = "›"
DIAMOND = "◆"
CIRCLE = "●"
STAR = "✦"
SPARK = "⚡"
GEAR = "⚙"
CHECK = "✓"
CROSS = "✗"
WARNING_ICON = "⚠"
LOCK = "🔒"
