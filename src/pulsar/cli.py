"""Pulsar CLI — The main entry point. This is what runs when you type 'pulsar'.

This file handles:
1. The Click CLI framework setup (--version, --provider, --model flags)
2. The main input loop (read user input → process → display)
3. Slash command routing (/help, /clear, /exit)
4. Graceful shutdown on Ctrl+C
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


# ═══════════════════════════════════════════════════════════════════
# SLASH COMMANDS
# ═══════════════════════════════════════════════════════════════════

def handle_slash_command(command: str) -> bool:
    """Handle slash commands. Returns True if the command was handled."""
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
        show_warning(f"Unknown command: {cmd}. Type /help for available commands.")
        return True


def _show_help() -> None:
    """Display available slash commands."""
    from rich.table import Table
    from pulsar.ui.themes import NEBULA, CYAN_GLOW, STARDUST, DUST

    console.print()
    table = Table(
        show_header=True,
        header_style=f"bold {CYAN_GLOW}",
        border_style=f"{DUST}",
        title="Commands",
        title_style=f"bold {NEBULA}",
        padding=(0, 2),
    )
    table.add_column("Command", style=f"bold {CYAN_GLOW}", min_width=12)
    table.add_column("Description", style=f"{STARDUST}")

    commands = [
        ("/help", "Show this help message"),
        ("/clear", "Clear the screen"),
        ("/version", "Show Pulsar version"),
        ("/demo", "Run a visual demo of all UI components"),
        ("/exit", "Exit Pulsar"),
    ]
    for cmd, desc in commands:
        table.add_row(cmd, desc)

    console.print(table)
    console.print()


def _run_demo() -> None:
    """Run a demo showcasing all UI components — for development/testing."""
    import time

    console.print()
    show_separator()
    show_info("Running UI component demo...")
    console.print()

    # 1. Thinking indicator
    show_thinking("Analyzing your codebase")
    time.sleep(0.5)

    # 2. Tool calls
    console.print()
    show_tool_call("read_file", {"path": "src/main.py"})
    show_tool_result("read_file", success=True)
    show_tool_output("def main():\n    print('Hello, Pulsar!')\n    return 0")

    console.print()
    show_tool_call("run_command", {"command": "pytest tests/"})
    show_tool_result("run_command", success=False)

    # 3. Permission request (auto-deny in demo)
    console.print()
    show_info("Permission prompt example (press 'n' or Enter to continue):")
    show_permission_request("Write File", "Create new file: src/pulsar/tools/git_status.py")

    # 4. Thinking content
    console.print()
    show_thinking_content(
        "The user wants to fix the login bug. I should:\n"
        "1. Read the auth module\n"
        "2. Find the validation logic\n"
        "3. Check the test file for expected behavior"
    )

    # 5. Response with markdown
    console.print()
    show_response(
        "I found the bug in `auth.py`. The issue is on **line 42** where "
        "the password hash comparison uses `==` instead of a "
        "constant-time comparison.\n\n"
        "```python\n"
        "# Before (vulnerable)\n"
        "if password_hash == stored_hash:\n\n"
        "# After (secure)\n"
        "import hmac\n"
        "if hmac.compare_digest(password_hash, stored_hash):\n"
        "```\n\n"
        "This prevents timing attacks. Want me to apply this fix?"
    )

    # 6. Token usage
    show_token_usage(1_847, 234, "gemini-2.5-flash")

    # 7. Status messages
    console.print()
    show_success("All 12 tests passing")
    show_warning("Large file detected (>500KB), consider chunking")
    show_error("API Error", "Rate limit exceeded. Retrying in 30s...")

    console.print()
    show_separator()
    show_info("Demo complete!")
    console.print()


# ═══════════════════════════════════════════════════════════════════
# INPUT LOOP
# ═══════════════════════════════════════════════════════════════════

def get_user_input() -> str:
    """Get input from the user using prompt_toolkit for better editing."""
    try:
        user_input = pt_prompt(
            HTML('<style fg="#c792ea" bold="true"> › </style>'),
        )
        return user_input.strip()
    except (EOFError, KeyboardInterrupt):
        return "/exit"


def input_loop() -> None:
    """The main interactive loop — read input, process, display."""
    while True:
        try:
            user_input = get_user_input()

            if not user_input:
                continue

            # Route slash commands
            if user_input.startswith("/"):
                handle_slash_command(user_input)
                continue

            # TODO: Day 2 — Send to LLM provider and get response
            # For now, echo back with a placeholder
            with thinking_spinner("Processing"):
                import time
                time.sleep(1)  # Simulate API call

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


# ═══════════════════════════════════════════════════════════════════
# CLI ENTRY POINT
# ═══════════════════════════════════════════════════════════════════

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
