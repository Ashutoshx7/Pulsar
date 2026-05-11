"""Pulsar application constants and default configuration."""

# ─── App Identity ──────────────────────────────────────────────────
APP_NAME = "Pulsar"
APP_TAGLINE = "Multi-Provider AI Coding Agent"
APP_VERSION = "0.1.0"

# ─── Model Defaults ────────────────────────────────────────────────
DEFAULT_PROVIDER = "gemini"
DEFAULT_MODEL = "gemini-2.5-flash"

# ─── Limits ─────────────────────────────────────────────────────────
MAX_TURNS = 50
COMMAND_TIMEOUT_SECONDS = 30
MAX_FILE_SIZE_BYTES = 512_000  # 500KB — don't read giant files

# ─── Paths ──────────────────────────────────────────────────────────
CONFIG_DIR_NAME = ".pulsar"
HISTORY_FILE = "history.json"
MEMORY_FILE = "memory.json"

# ─── UI ─────────────────────────────────────────────────────────────
INPUT_PROMPT = "›"
THINKING_MESSAGE = "Thinking..."
MAX_DISPLAY_LINES = 200
