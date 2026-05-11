"""Pulsar CLI — Main entry point.

Handles: Click CLI, input loop, slash commands, graceful shutdown.
"""

import click
from prompt_toolkit import prompt as pt_prompt
from prompt_toolkit.formatted_text import HTML

from pulsar import __version__
from pulsar.ui.console import console
from pulsar.ui.display import (
    show_welcome,
    show_response,
    show_tool_call,
    show_tool_result,
    show_tool_output,
    show_thinking,
    show_thinking_content,
    show_token_usage,
    show_error,
    show_warning,
    show_success,
    show_info,
    show_permission_request,
    show_separator,
    show_goodbye,
    # Stolen features
    show_diff,
    show_files_in_context,
    show_plan,
    show_edit_preview,
    show_status_bar,
    show_cost,
    show_session_summary,
)
from pulsar.ui.spinner import thinking_spinner
from pulsar.ui.themes import NEBULA, CYAN_GLOW, STARDUST, DUST, PLASMA


# ─── Slash Commands ─────────────────────────────────────────────────

def handle_slash_command(command: str) -> bool:
    """Handle slash commands. Returns True if handled."""
    cmd = command.strip().lower()

    if cmd in ("/exit", "/quit", "/q"):
        show_goodbye()
        raise SystemExit(0)

    elif cmd == "/help":
        _show_help()
        return True

    elif cmd == "/clear":
        console.clear()
        show_welcome()
        return True

    elif cmd == "/version":
        show_info(f"Pulsar v{__version__}")
        return True

    elif cmd == "/demo":
        _run_demo()
        return True

    else:
        show_warning(f"Unknown command: {cmd}. Type /help for commands.")
        return True


def _show_help() -> None:
    """Display commands in a cosmic styled table."""
    from rich.table import Table
    from pulsar.ui.themes import DEEP_GRAY

    console.print()
    table = Table(
        show_header=True,
        header_style=f"bold {CYAN_GLOW}",
        border_style=f"{DEEP_GRAY}",
        title="Commands",
        title_style=f"bold {NEBULA}",
        padding=(0, 2),
    )
    table.add_column("Command", style=f"bold {CYAN_GLOW}", min_width=12)
    table.add_column("Description", style=f"{STARDUST}")

    commands = [
        ("/help", "Show this help message"),
        ("/clear", "Clear screen"),
        ("/version", "Show Pulsar version"),
        ("/model", "Switch model (coming soon)"),
        ("/demo", "Preview all UI components"),
        ("/exit", "Exit Pulsar"),
    ]
    for cmd, desc in commands:
        table.add_row(cmd, desc)

    console.print(table)
    console.print()


def _run_demo() -> None:
    """Demo showcasing ALL UI components — original + stolen features."""
    import time

    console.print()
    show_separator()
    show_info("Running UI demo — all components...")
    console.print()

    # ── STOLEN: Files in context (from Aider) ──
    show_files_in_context([
        "src/auth.py",
        "src/models/user.py",
        "tests/test_auth.py",
    ])

    # ── Thinking (original) ──
    show_thinking("Analyzing your codebase")
    console.print()

    show_thinking_content(
        "The user wants to fix the login bug.\n"
        "1. Read the auth module\n"
        "2. Find the validation logic\n"
        "3. Check test expectations"
    )

    # ── STOLEN: Plan display (from Codex CLI) ──
    show_plan([
        "Read src/auth.py to find the bug",
        "Edit the password comparison logic",
        "Run tests to verify the fix",
    ])

    # ── Tool calls (original + enhanced) ──
    show_tool_call("read_file", {"path": "src/auth.py"})
    show_tool_result("read_file", success=True)
    show_tool_output(
        "def verify_password(password, stored_hash):\n"
        "    password_hash = hash_password(password)\n"
        "    if password_hash == stored_hash:  # BUG\n"
        "        return True\n"
        "    return False"
    )
    console.print()

    # ── STOLEN: Edit preview (from Codex CLI) ──
    show_edit_preview(
        "src/auth.py", 42,
        "    if password_hash == stored_hash:",
        "    if hmac.compare_digest(password_hash, stored_hash):",
    )

    # ── Permission (original, panel style) ──
    show_permission_request("Write File", "src/auth.py (1 line changed)")
    console.print()

    show_tool_call("edit_file", {"path": "src/auth.py"})
    show_tool_result("edit_file", success=True)
    console.print()

    # ── STOLEN: Diff viewer (from Aider) ──
    show_diff(
        "src/auth.py",
        "    if password_hash == stored_hash:\n        return True",
        "    if hmac.compare_digest(password_hash, stored_hash):\n        return True",
    )

    # ── Tool: run tests ──
    show_tool_call("run_command", {"command": "pytest tests/ -x"})
    show_tool_result("run_command", success=True)
    console.print()

    # ── Response (original, markdown) ──
    show_response(
        "Fixed the timing attack in `auth.py`. "
        "Now uses `hmac.compare_digest()` for constant-time comparison.\n\n"
        "```python\n"
        "import hmac\n"
        "if hmac.compare_digest(password_hash, stored_hash):\n"
        "```\n\n"
        "All tests passing."
    )

    # ── STOLEN: Cost display (from Aider) ──
    show_cost(1_847, 234, "gemini-2.5-flash", 0.0012)

    # ── Status messages (original) ──
    console.print()
    show_success("All 12 tests passing")
    show_warning("Large file detected (>500KB)")
    show_error("API Error", "Rate limit exceeded. Retrying in 30s...")

    # ── STOLEN: Status bar (from Claude Code) ──
    show_status_bar(
        model="gemini-2.5-flash",
        total_tokens=4_231,
        total_cost=0.0034,
        turn=3,
    )

    # ── STOLEN: Session summary (end of session) ──
    show_session_summary(
        turns=3,
        total_tokens=4_231,
        total_cost=0.0034,
        duration_secs=127,
    )

    show_info("Demo complete!")
    console.print()


# ─── Input Loop ─────────────────────────────────────────────────────

def get_user_input() -> str:
    """Get input using prompt_toolkit with cosmic styling."""
    try:
        user_input = pt_prompt(
            HTML('<style fg="#c792ea" bold="true"> › </style>'),
        )
        return user_input.strip()
    except (EOFError, KeyboardInterrupt):
        return "/exit"


def input_loop() -> None:
    """Main interactive loop."""
    while True:
        try:
            user_input = get_user_input()

            if not user_input:
                continue

            if user_input.startswith("/"):
                handle_slash_command(user_input)
                continue

            # TODO: Day 2 — send to Gemini provider
            with thinking_spinner("Processing"):
                import time
                time.sleep(1)

            show_response(
                f"**Echo mode** — LLM provider not connected yet.\n\n"
                f"You said: *\"{user_input}\"*\n\n"
                f"Connect a provider on Day 2 to get real responses."
            )
            show_token_usage(0, 0, "none")

        except KeyboardInterrupt:
            console.print()
            show_goodbye()
            break
        except SystemExit:
            break


# ─── Entry Point ────────────────────────────────────────────────────

@click.command()
@click.version_option(version=__version__, prog_name="Pulsar")
@click.option("--provider", default="gemini", help="LLM provider to use")
@click.option("--model", default=None, help="Specific model to use")
def main(provider: str, model: str) -> None:
    """Pulsar — Multi-Provider AI Coding Agent"""
    show_welcome()
    input_loop()


if __name__ == "__main__":
    main()
