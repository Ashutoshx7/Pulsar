<div align="center">

```
██████╗ ██╗   ██╗██╗     ███████╗ █████╗ ██████╗
██╔══██╗██║   ██║██║     ██╔════╝██╔══██╗██╔══██╗
██████╔╝██║   ██║██║     ███████╗███████║██████╔╝
██╔═══╝ ██║   ██║██║     ╚════██║██╔══██║██╔══██╗
██║     ╚██████╔╝███████╗███████║██║  ██║██║  ██║
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
```

### The terminal AI coding agent that works with any model

<br/>

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-F97316?style=for-the-badge)](https://github.com/Ashutoshx7/Pulsar/releases)

<br/>

> **Use any AI model. Pay nothing. Extend everything.**

<br/>

[Get Started](#install) · [Features](#features) · [Architecture](#architecture) · [Roadmap](#roadmap) · [Contributing](#contributing)

</div>

<br/>

---

## Why Pulsar?

Every other terminal coding agent is locked to one company's model. Claude Code needs Anthropic. Codex needs OpenAI. Gemini CLI needs Google.

Pulsar works with all of them. Free Gemini by default. Switch to Claude for complex reasoning. Run Llama locally with Ollama when you need privacy. One beautiful interface, any brain.

<br/>

<div align="center">

| | Claude Code | Aider | Codex CLI | **Pulsar** |
|:--|:--:|:--:|:--:|:--:|
| Multi-provider | ❌ | ✅ | ❌ | ✅ |
| Native tool calling | ✅ | ❌ | ✅ | ✅ |
| Rich terminal UI | ✅ | ❌ | ❌ | ✅ |
| MCP support | ✅ | ❌ | ✅ | 🔜 |
| Plugin system | ❌ | ❌ | ❌ | 🔜 |
| Free by default | ❌ | ✅ | ❌ | ✅ |
| Fully open source | ❌ | ✅ | ✅ | ✅ |

</div>

<br/>

---

## Features

<br/>

<div align="center">

**⚡ Agentic Loop** · **🎨 Premium TUI** · **🔧 6 Tools** · **🔒 Permission System** · **🌐 Multi-Provider**

</div>

<br/>

**The Agent**

The core is a multi-turn agentic loop powered by native function calling. Pulsar reads your files, edits code, runs commands, searches your codebase, and commits to git. All while streaming responses in real time. When something requires your approval, it stops and asks. Every destructive action needs your explicit yes.

**The Interface**

Pulsar has a cosmic-themed terminal UI built with Rich. Responses stream word by word with syntax-highlighted code blocks. Tool calls appear with a warm orange icon as they happen. File diffs show green additions and red removals inline. A persistent status bar tracks your model, turn count, and session cost. When you exit, a summary shows total tokens and time spent.

**The Philosophy**

No vendor lock-in. No mandatory subscriptions. Transparent costs. Full control over what runs on your machine.

<br/>

---

## Install

```bash
pip install pulsar-agent
```

Or install from source for the latest changes:

```bash
git clone https://github.com/Ashutoshx7/Pulsar.git
cd Pulsar
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

<br/>

---

## Setup

**1. Get a free API key**

Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey) and create a key. The free tier gives you more than enough to work with.

**2. Add it to your project**

```bash
echo "GOOGLE_API_KEY=your_key_here" > .env
```

**3. Run it**

```bash
pulsar
```

<br/>

---

## Usage

Type any coding task in plain English:

```
› Fix the timing attack vulnerability in src/auth.py
› Add type hints to all functions in utils.py
› Write tests for the UserService class
› Refactor the database module to use async/await
› Explain what this codebase does
```

Pulsar will plan the approach, show you each step, ask for approval before touching your files, and report results.

**Slash commands available inside Pulsar:**

| Command | What it does |
|:--------|:-------------|
| `/help` | Show all commands |
| `/demo` | Preview every UI component |
| `/model` | Switch provider or model |
| `/clear` | Clear the screen |
| `/version` | Show current version |
| `/exit` | Quit Pulsar |

<br/>

---

## Architecture

Pulsar is built around two core patterns that make it extensible.

**Adapter Pattern for Providers**

Every AI provider implements the same `LLMProvider` abstract class. The agentic loop never knows which model it is talking to. Adding a new provider means writing one class. Nothing else changes.

```python
class LLMProvider(ABC):
    @abstractmethod
    def chat(self, messages, tools) -> LLMResponse: ...

    @abstractmethod
    def stream(self, messages, tools) -> Iterator[str]: ...
```

**Registry Pattern for Tools**

Every tool registers itself with the `ToolRegistry`. The agent calls tools by name. Adding a new tool means writing one class and one line of registration code.

```python
registry = ToolRegistry()
registry.register(ReadFileTool())
registry.register(WriteFileTool())
registry.register(RunCommandTool())
```

**The Agentic Loop**

```
You type a message
        ↓
Sent to model with tool declarations
        ↓
Model wants to call a tool?
    ├── Yes → Run tool → Send result back → repeat
    └── No  → Stream final answer to you
```

<br/>

**Project layout:**

```
src/pulsar/
├── cli.py                  Entry point and input loop
├── agent/
│   ├── loop.py             The agentic loop
│   └── messages.py         Conversation history manager
├── llm/
│   ├── base.py             LLMProvider abstract class
│   └── gemini.py           Gemini 2.5 Flash implementation
├── tools/
│   ├── registry.py         Tool registry and executor
│   ├── read_file.py        Read any file
│   ├── write_file.py       Create new files
│   ├── edit_file.py        Surgical find-and-replace edits
│   ├── run_command.py      Shell commands with approval
│   └── search_files.py     Search across your codebase
├── ui/
│   ├── themes.py           Color palette and icons
│   ├── console.py          Global Rich console instance
│   ├── display.py          Every visual component
│   └── spinner.py          Animated thinking indicator
└── config/
    └── __init__.py         App constants and defaults
```

<br/>

---

## Roadmap

<br/>

<div align="center">

```
v0.1.0   v0.2.0   v0.3.0   v0.4.0   v0.5.0   v1.0.0
  UI   →  Agent  →  Multi  →  MCP   →  Smart  →  Ship
 Done    In Dev   Provider  Plugins  Memory   Prod
```

</div>

<br/>

**v0.1.0** · UI system, CLI skeleton, slash commands, demo mode ✅

**v0.2.0** · Gemini provider connected, full agentic loop, 6 tools, file editing 🔧

**v0.3.0** · Claude, GPT-4o, and Ollama providers, live model switching 🔜

**v0.4.0** · MCP protocol client, Python plugin system 🔜

**v0.5.0** · Codebase indexing, web search, persistent memory 🔜

**v1.0.0** · Headless CI mode, Docker sandbox, auto-loop for autonomous tasks 🔜

<br/>

---

## Contributing

Pulsar is actively being built in public. Contributions are welcome at any stage.

```bash
git clone https://github.com/Ashutoshx7/Pulsar.git
cd Pulsar
python -m venv .venv && source .venv/bin/activate
pip install -e .
pulsar --version
```

Open an issue before starting large changes. Small fixes and improvements can go straight to a pull request.

<br/>

---

<div align="center">

Built with Python · Powered by [Gemini](https://aistudio.google.com) · Inspired by Claude Code, Aider, and Codex CLI

<br/>

*If this project is useful to you, consider giving it a star.*

[![Star on GitHub](https://img.shields.io/github/stars/Ashutoshx7/Pulsar?style=social)](https://github.com/Ashutoshx7/Pulsar)

</div>
