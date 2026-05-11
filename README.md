<div align="center">

```
 ██████╗ ██╗   ██╗██╗     ███████╗ █████╗ ██████╗ 
 ██╔══██╗██║   ██║██║     ██╔════╝██╔══██╗██╔══██╗
 ██████╔╝██║   ██║██║     ███████╗███████║██████╔╝ 
 ██╔═══╝ ██║   ██║██║     ╚════██║██╔══██║██╔══██╗
 ██║     ╚██████╔╝███████╗███████║██║  ██║██║  ██║
 ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
```


<br/>

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Models](https://img.shields.io/badge/Models-Gemini%20%7C%20Claude%20%7C%20GPT%20%7C%20Ollama-c792ea?style=for-the-badge&logoColor=white)](#-roadmap)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-f78c6c?style=for-the-badge)](https://github.com/Ashutoshx7/Pulsar/releases)
[![Stars](https://img.shields.io/github/stars/Ashutoshx7/Pulsar?style=for-the-badge&color=ffcb6b&logo=github&logoColor=white)](https://github.com/Ashutoshx7/Pulsar)

<br/>

**Use any AI model. Pay nothing. Extend everything.**

<br/>

[Get Started](#-install) &nbsp;&nbsp;|&nbsp;&nbsp; [Features](#-features) &nbsp;&nbsp;|&nbsp;&nbsp; [Architecture](#-architecture) &nbsp;&nbsp;|&nbsp;&nbsp; [Roadmap](#-roadmap) &nbsp;&nbsp;|&nbsp;&nbsp; [Contributing](#-contributing)

<br/>

</div>

<br/>

## Why Pulsar?

Every other terminal coding agent locks you to one company.

> Claude Code needs Anthropic. Codex needs OpenAI. Gemini CLI needs Google.

Pulsar breaks that. Use free Gemini by default. Switch to Claude for complex reasoning. Run Llama locally with Ollama for total privacy. One beautiful interface, any brain, on your terms.

<br/>

<div align="center">

|  | Claude Code | Aider | Codex CLI | **Pulsar** |
|:--|:--:|:--:|:--:|:--:|
| Multi-provider support | ❌ | ✅ | ❌ | ✅ |
| Native function calling | ✅ | ❌ | ✅ | ✅ |
| Premium terminal UI | ✅ | ❌ | ❌ | ✅ |
| Inline git diff display | ❌ | ✅ | ❌ | ✅ |
| Plan before execution | ❌ | ❌ | ✅ | ✅ |
| Session cost tracking | ✅ | ✅ | ❌ | ✅ |
| MCP support | ✅ | ❌ | ✅ | 🔜 |
| Plugin system | ❌ | ❌ | ❌ | 🔜 |
| Free by default | ❌ | ✅ | ❌ | ✅ |
| Open source | ❌ | ✅ | ✅ | ✅ |

</div>

<br/>

## ✦ Features

<br/>

<table>
<tr>
<td width="50%">

### ⚡ Agentic Loop

Multi-turn function calling loop. Pulsar reads files, edits code, runs tests, and searches your codebase. It streams results live and stops for approval before anything destructive.

</td>
<td width="50%">

### 🎨 Cosmic Terminal UI

Built with Rich. Syntax-highlighted code, animated thinking spinner, colored git diffs, persistent status bar, session cost tracking, and a stunning welcome banner.

</td>
</tr>
<tr>
<td width="50%">

### 🌐 Any Model, Any Time

Gemini 2.5 Flash free by default. Switch to Claude, GPT-4o, or local Ollama with one command. The adapter pattern means adding a new provider is just one class.

</td>
<td width="50%">

### 🔒 Permission System

Every file write and shell command requires your approval. You see the full edit preview before anything is touched. Three modes: suggest, auto-edit, or full auto.

</td>
</tr>
<tr>
<td width="50%">

### 📋 Plan Before Execute

Stolen from Codex CLI. Pulsar shows you a numbered plan of what it intends to do before it does anything. You see the full picture, not just one step at a time.

</td>
<td width="50%">

### 🔧 Extensible Tools

Read files, write files, surgical edits, run shell commands, search codebase, list directories. More tools coming. Plugin system in v0.4.0.

</td>
</tr>
</table>

<br/>

## 📦 Install

**From PyPI:**

```bash
pip install pulsar-agent
```

**From source:**

```bash
git clone https://github.com/Ashutoshx7/Pulsar.git
cd Pulsar
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

<br/>

## ⚙️ Setup

**Step 1. Get a free Gemini API key**

Visit [aistudio.google.com/apikey](https://aistudio.google.com/apikey). The free tier has a generous limit, more than enough for daily coding use.

**Step 2. Add it to your project**

```bash
echo "GOOGLE_API_KEY=your_key_here" > .env
```

**Step 3. Launch Pulsar**

```bash
pulsar
```

<br/>

## 💬 Usage

Type any task in natural language:

```
 › Fix the timing attack vulnerability in src/auth.py
 › Add type hints to every function in utils.py
 › Write tests for the UserService class
 › Refactor the database layer to use async/await
 › What does this codebase actually do?
```

Pulsar plans the approach, previews every change, asks for approval, and reports the result.

**Commands inside Pulsar:**

| Command | Description |
|:--------|:------------|
| `/help` | Show all commands |
| `/demo` | Preview every UI component live |
| `/model` | Switch provider or model |
| `/clear` | Clear the terminal |
| `/version` | Show current version |
| `/exit` | Quit Pulsar |

<br/>

## 🏗 Architecture

Pulsar is built on two patterns that keep everything modular.

**Provider Adapter**

Every AI model implements one interface. The agentic loop never knows which model it is talking to. Swap providers without touching the loop.

```python
class LLMProvider(ABC):
    @abstractmethod
    def chat(self, messages, tools) -> LLMResponse: ...

    @abstractmethod
    def stream(self, messages, tools) -> Iterator[str]: ...
```

**Tool Registry**

Tools register themselves. The agent calls them by name. Adding a new tool is one class and one line.

```python
registry = ToolRegistry()
registry.register(ReadFileTool())
registry.register(WriteFileTool())
registry.register(RunCommandTool())
```

**The Loop**

```
 › You send a message
        ↓
 Sent to model with all tool declarations
        ↓
 Model calls a tool?
    ├── Yes  →  Run tool  →  Send result back  →  repeat
    └── No   →  Stream final answer to terminal
```

**Project structure:**

```
src/pulsar/
├── cli.py                  Entry point, input loop, slash commands
├── agent/
│   ├── loop.py             The agentic loop
│   └── messages.py         Conversation history and compaction
├── llm/
│   ├── base.py             LLMProvider abstract class
│   ├── gemini.py           Gemini implementation
│   └── ollama.py           Ollama (local) implementation
├── tools/
│   ├── registry.py         Tool registry and executor
│   ├── read_file.py        Read any file into context
│   ├── write_file.py       Create files with approval
│   ├── edit_file.py        Surgical find and replace
│   ├── run_command.py      Shell commands with approval
│   └── search_files.py     Ripgrep-powered codebase search
├── ui/
│   ├── themes.py           Color palette and icon system
│   ├── console.py          Global Rich console
│   ├── display.py          Every visual component
│   └── spinner.py          Animated thinking indicator
└── config/
    └── __init__.py         App constants and defaults
```

<br/>

## 🗺 Roadmap

<br/>

<div align="center">

| Version | Focus | Status |
|:-------:|:------|:------:|
| `v0.1.0` | UI system, CLI skeleton, slash commands, cosmic theme | ✅ Done |
| `v0.2.0` | Gemini provider, agentic loop, 6 tools, file editing | 🔧 Building |
| `v0.3.0` | Claude, GPT-4o, Ollama support, live model switching | 🔜 |
| `v0.4.0` | MCP protocol client, Python plugin system | 🔜 |
| `v0.5.0` | Codebase indexing, web search, persistent memory | 🔜 |
| `v1.0.0` | Headless CI mode, Docker sandbox, auto-loop | 🔜 |

</div>

<br/>

## 🤝 Contributing

Pulsar is built in public. All contributions are welcome.

```bash
git clone https://github.com/Ashutoshx7/Pulsar.git
cd Pulsar
python -m venv .venv && source .venv/bin/activate
pip install -e .
pulsar --version
# type /demo to see the full UI
```

Open an issue before large changes. Small fixes can go straight to a PR.

<br/>

---

<div align="center">

Built with Python &nbsp;·&nbsp; Works with any LLM &nbsp;·&nbsp; Inspired by Claude Code, Aider, and Codex CLI

<br/>

**If Pulsar is useful to you, a star means a lot.**

[![Star on GitHub](https://img.shields.io/github/stars/Ashutoshx7/Pulsar?style=for-the-badge&color=ffcb6b&logo=github)](https://github.com/Ashutoshx7/Pulsar)

</div>
