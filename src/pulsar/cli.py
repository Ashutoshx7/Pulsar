"""Pulsar CLI — Main entry point.

Handles:
1. Click CLI setup (--version, --provider, --model)
2. Interactive input loop
3. Slash command routing
4. Graceful shutdown
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
)
from pulsar.ui.spinner import thinking_spinner


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
        show_info(f"pulsar v{__version__}")
        return True

    elif cmd == "/demo":
        _run_demo()
        return True

    else:
        show_warning(f"unknown command: {cmd}")
        return True


def _show_help() -> None:
    """Minimal help display."""
    from pulsar.ui.themes import FG, FG_MUTED, FG_DIM, CYAN, ACCENT
    from rich.text import Text

    console.print()
    commands = [
        ("/help", "show this message"),
        ("/clear", "clear screen"),
        ("/version", "show version"),
        ("/model", "switch model (coming soon)"),
        ("/demo", "preview all UI components"),
        ("/exit", "quit pulsar"),
    ]
    for cmd, desc in commands:
        line = Text()
        line.append(f"  {cmd:<12}", style=f"bold {CYAN}")
        line.append(desc, style=f"{FG_DIM}")
        console.print(line)
    console.print()


def _run_demo() -> None:
    """Demo all UI components — for development/testing."""
    import time

    console.print()
    show_separator()
    show_info("running UI demo...")
    console.print()

    # Thinking
    show_thinking("analyzing codebase")
    console.print()

    # Thinking content (model reasoning)
    show_thinking_content(
        "The user wants to fix the login bug.\n"
        "1. Read the auth module\n"
        "2. Find the validation logic\n"
        "3. Check test expectations"
    )

    # Tool calls
    show_tool_call("read_file", {"path": "src/auth.py"})
    show_tool_result("read_file", success=True)
    show_tool_output(
        "def verify_password(password, stored_hash):\n"
        "    password_hash = hash_password(password)\n"
        "    if password_hash == stored_hash:  # BUG: timing attack\n"
        "        return True\n"
        "    return False"
    )
    console.print()

    show_tool_call("edit_file", {"path": "src/auth.py", "old": "==", "new": "hmac.compare_digest"})
    show_tool_result("edit_file", success=True)
    console.print()

    show_tool_call("run_command", {"command": "pytest tests/ -x"})
    show_tool_result("run_command", success=False)
    console.print()

    # Permission
    show_info("permission prompt example:")
    show_permission_request("write file", "src/auth.py (3 lines changed)")
    console.print()

    # Response
    show_response(
        "Fixed the timing attack vulnerability in `auth.py`. "
        "The password comparison now uses `hmac.compare_digest()` "
        "instead of `==`.\n\n"
        "```python\n"
        "import hmac\n"
        "if hmac.compare_digest(password_hash, stored_hash):\n"
        "```\n\n"
        "All tests passing."
    )

    # Token usage
    show_token_usage(1_847, 234, "gemini-2.5-flash")

    # Status messages
    console.print()
    show_success("12 tests passing")
    show_warning("large file detected (>500KB)")
    show_error("rate limit", "retrying in 30s...")

    show_separator()
    show_info("demo complete")
    console.print()


# ─── Input Loop ─────────────────────────────────────────────────────

def get_user_input() -> str:
    """Get input using prompt_toolkit."""
    try:
        user_input = pt_prompt(
            HTML('<style fg="#a78bfa" bold="true"> ❯ </style>'),
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

            # TODO: Day 2 — send to LLM provider
            with thinking_spinner("processing"):
                import time
                time.sleep(1)

            show_response(
                f"*echo mode* — no provider connected yet.\n\n"
                f"> {user_input}\n\n"
                f"Connect Gemini on Day 2 to get real responses."
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
@click.version_option(version=__version__, prog_name="pulsar")
@click.option("--provider", default="gemini", help="LLM provider")
@click.option("--model", default=None, help="Model to use")
def main(provider: str, model: str) -> None:
    """pulsar — multi-provider AI coding agent"""
    show_welcome()
    input_loop()


if __name__ == "__main__":
    main()
