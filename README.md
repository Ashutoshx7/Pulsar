<div align="center">

```
 ██████╗ ██╗   ██╗██╗     ███████╗ █████╗ ██████╗
 ██╔══██╗██║   ██║██║     ██╔════╝██╔══██╗██╔══██╗
 ██████╔╝██║   ██║██║     ███████╗███████║██████╔╝
 ██╔═══╝ ██║   ██║██║     ╚════██║██╔══██║██╔══██╗
 ██║     ╚██████╔╝███████╗███████║██║  ██║██║  ██║
 ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
```

**Multi-Provider AI Coding Agent for the Terminal**

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-cyan?style=flat-square)](https://github.com/Ashutoshx7/Pulsar)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green?style=flat-square)](https://github.com/Ashutoshx7/Pulsar/pulls)

*Use any AI model. Pay nothing. Extend everything.*

</div>

---

## What is Pulsar?

Pulsar is a terminal-based AI coding agent that runs in your existing terminal. You bring a task, Pulsar reads your files, edits your code, runs your tests, and reports back. All through a streaming, beautifully rendered interface.

Unlike other coding agents, Pulsar is not locked to a single AI provider. Today you can use the free Gemini tier. Tomorrow you switch to Claude for a tricky refactor. On a plane with no internet, you run a local Llama model through Ollama. One tool, any brain.

## Features

**Core Agent**

- Agentic loop with native function calling
- Streaming responses rendered in real time
- Full markdown and syntax-highlighted code output
- Permission-based security for all file writes and shell commands
- Git-aware context injection (current branch, changed files)

**Premium Terminal UI**

- Cosmic-themed interface with color-coded status
- Animated thinking spinner while the agent processes
- Plan display before execution, inspired by Codex CLI
- Colored git diff output for every file edit, inspired by Aider
- File context tracker showing what the agent is working with
- Dollar cost and token count after every response, inspired by Aider
- Persistent status bar showing model, turn count and session cost, inspired by Claude Code
- Session summary on exit with full stats

**Tools the Agent Can Use**

- Read, write, and edit files with surgical precision
- Run shell commands with your approval
- Search across your codebase
- List directory trees
- Run git operations

**Multi-Provider Support** *(coming in v0.3.0)*

- Gemini 2.5 Flash (default, free tier)
- Claude Sonnet and Opus
- GPT-4o and GPT-4o-mini
- Ollama for fully local, offline, private usage

## Install

```bash
pip install pulsar-agent
```

Or clone and install from source:

```bash
git clone https://github.com/Ashutoshx7/Pulsar.git
cd Pulsar
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Setup

Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey) and create a `.env` file:

```bash
echo "GOOGLE_API_KEY=your_key_here" > .env
```

## Usage

```bash
pulsar
```

Type any coding task in natural language:

```
› Fix the authentication bug in src/auth.py
› Add type hints to all functions in utils.py
› Write tests for the payment module
› Refactor this class to use dataclasses
```

## Slash Commands

| Command | Description |
|---------|-------------|
| `/help` | Show all available commands |
| `/clear` | Clear the screen |
| `/model` | Switch AI provider or model |
| `/demo` | Preview all UI components |
| `/version` | Show current version |
| `/exit` | Quit Pulsar |

## Demo Mode

Type `/demo` inside Pulsar to see a full walkthrough of every UI component. It simulates a real agent session including plan display, tool calls, file diffs, permission prompts, and session stats.

## Architecture

Pulsar is built on three core principles:

**Adapter Pattern for Providers**
Every AI provider (Gemini, Claude, OpenAI, Ollama) implements the same `LLMProvider` interface. The agentic loop never knows which model it is talking to. Switching providers is a config change, not a code change.

**Registry Pattern for Tools**
Every tool (read file, write file, run command, search) registers itself with the `ToolRegistry`. The agent loop calls tools by name. Adding a new tool means writing one class and registering it. Nothing else changes.

**Agentic Loop**
The loop sends your message to the model with all tool declarations. If the model responds with a tool call, Pulsar runs it and sends the result back. This continues until the model produces a final text response. The loop handles multiple parallel tool calls, error recovery, and token tracking.

```
User Input
    ↓
Send to Model (with tool declarations)
    ↓
Model responds with tool call(s)?
    ├── Yes → Run tools → Send results back → repeat
    └── No  → Stream final response to user
```

## Project Structure

```
src/pulsar/
├── cli.py              Entry point and input loop
├── agent/
│   ├── loop.py         The agentic loop
│   └── messages.py     Conversation history manager
├── llm/
│   ├── base.py         LLMProvider abstract class
│   └── gemini.py       Gemini implementation
├── tools/
│   ├── registry.py     Tool registry
│   ├── read_file.py    Read file tool
│   ├── write_file.py   Write file tool
│   ├── edit_file.py    Edit file tool
│   └── run_command.py  Shell command tool
├── ui/
│   ├── themes.py       Color system and icons
│   ├── console.py      Global Rich console
│   ├── display.py      All visual components
│   └── spinner.py      Animated thinking indicator
└── config/
    └── __init__.py     Constants and defaults
```

## Roadmap

**v0.1.0** (current) · UI system, CLI skeleton, slash commands, demo mode

**v0.2.0** · Gemini provider connected, full agentic loop, 6 tools, file editing with permission prompts

**v0.3.0** · Multi-provider support (Claude, GPT-4o, Ollama), live model switching

**v0.4.0** · MCP protocol client, Python plugin system

**v0.5.0** · Codebase indexing, web search, persistent memory

**v1.0.0** · Headless CI mode, Docker sandbox, auto-loop

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

```bash
git clone https://github.com/Ashutoshx7/Pulsar.git
cd Pulsar
python -m venv .venv && source .venv/bin/activate
pip install -e .
pulsar --version
```

## License

[MIT](LICENSE)

---

<div align="center">

Built with Python · Powered by Gemini · Open Source

*Freedom of choice. Free by default. Extensible by design.*

</div>
