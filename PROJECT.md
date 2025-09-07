# PROJECT.md

## 📌 Project Overview

This project is a **personal and continuously customizable personal assistant** built using [LangGraph](https://www.langchain.com/langgraph).
The assistant will run locally in a containerized environment and interact with personal files, Google Calendar, and a goal-tracking system.

The assistant will serve as:

* A conversational interface for managing goals, tasks, and schedules.
* An organizer that integrates goals into actionable milestones and calendar events.
* A knowledge assistant that can read and answer questions about project folders.
* A productivity tool with **undoable changes** tracked via Git.

---

## ✨ Key Features

1. **Project Folder Assistant**

   * Reads and indexes project directories.
   * Answers questions about files and codebases via RAG (retrieval-augmented generation).

2. **Google Calendar Integration**

   * **Phase 1**: Read-only access to Primary calendar for conflict detection.
   * **Phase 2**: Write to a **sandbox calendar** for safe planning.
   * **Phase 3 (opt-in)**: Explicit toggle to write directly to Primary calendar with confirmation.
   * Creates reminders and recurring tasks.

3. **Goal Management System**

   * Maintains a human-friendly, editable `goals.md` (Markdown with frontmatter) or `goals.yaml`.
   * Each goal has:

     * Title
     * Priority
     * Intended completion date
     * Milestones
   * Assistant can add, update, and track goals conversationally.

4. **Schedule Planner**

   * Uses goals to propose weekly/monthly plans.
   * Balances priority, deadlines, and recurring tasks.
   * Shows **dry-run previews** (diffs for file changes, preview of proposed calendar events) before applying.

5. **Undo & Version Control**

   * All file changes tracked via **Git** (automatic commits per change).
   * “Undo” support via Git revert or by reverting a specific operation.
   * Calendar events are tagged with metadata for safe deletion/rollback.

6. **Conversational Interface**

   * Natural language interface via CLI (initial) or minimal Web UI.
   * Allows managing goals, tasks, and schedules through chat.

---

## 🛠️ Tech Stack

* **Core Orchestration**: [LangGraph](https://www.langchain.com/langgraph) (deterministic, tool-calling flows).
* **LLMs**:

  * Local: [Ollama](https://ollama.ai/) with **Llama 3.1 8B** (default), optional larger models (70B) if GPU available.
  * Fallback: OpenAI/Anthropic APIs (configurable).
* **Embeddings & Retrieval**:

  * [LanceDB](https://lancedb.com/) (embedded vector DB with schema + filtering).
  * Embedding model: `nomic-embed-text` (local) or OpenAI embeddings.
* **Application Server**: [FastAPI](https://fastapi.tiangolo.com/) for API + orchestration endpoints.
* **Background Jobs (optional)**: RQ or Celery with Redis.
* **File Handling**: Local filesystem with [watchdog](https://github.com/gorakhargosh/watchdog) for auto-indexing changes.
* **State & Undo**: [Git](https://git-scm.com/) (via [GitPython](https://gitpython.readthedocs.io/)) + custom `ops/` ledger.
* **Calendar Integration**: [Google Calendar API](https://developers.google.com/calendar) via `google-api-python-client` or `gcsa`.

  * Sandbox calendar for safe writes.
  * Primary calendar writes only after explicit user opt-in.
* **Containerization**: Docker + `docker-compose`

  * `app`: FastAPI + LangGraph + tooling
  * `ollama`: local LLM server (with GPU passthrough if available)
  * `vector-db`: LanceDB (via volume)
  * `redis`: optional queue/cache
* **Observability**: `loguru` for structured logs, optional OpenTelemetry.

---

## 📂 Repository Structure

```
project-assistant/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entrypoint + LangGraph integration
│   ├── agents/              # LangGraph agent definitions and flows
│   │   ├── planner.py
│   │   ├── repo_assistant.py
│   │   ├── calendar_tools.py
│   │   └── goals_tools.py
│   ├── services/            # Service layers
│   │   ├── git_service.py
│   │   ├── calendar_service.py
│   │   ├── file_watcher.py
│   │   └── embeddings.py
│   ├── models/              # Pydantic schemas (Goal, Milestone, ChangePlan, etc.)
│   ├── ops/                 # Operation log + undo handlers
│   └── utils/               # Logging, config, helpers
│
├── goals/
│   ├── goals.md              # Human-readable goals (with frontmatter metadata)
│   └── index.yaml            # Machine-readable index of goals/milestones
│
├── .assistant/               # Internal state, volumes, indices, tokens
│   ├── lance/                # LanceDB storage
│   ├── sqlite/               # (optional) local SQL metadata
│   ├── faiss/                # (optional) FAISS index files if used
│   └── ops/                  # Operation logs for undo
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example              # Environment variable template (API keys, model config)
└── PROJECT.md                # Project documentation
```

---

## 🎯 Milestones

### Phase 1 – Foundation

*

### Phase 2 – Calendar (Sandbox Mode)

*

### Phase 3 – Goal Management

*

### Phase 4 – Planning Loop

*

### Phase 5 – UX & Primary Calendar Integration

*

---

## 📈 Progress Tracking

| Date       | Update                                                                                                                                           
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ 
| 2025-09-06 | Project initialized. Added initial `PROJECT.md`.
| 2025-09-07 | Defined tech stack (LangGraph, Ollama, LanceDB, FastAPI, Git, Docker, Google Calendar). Updated milestones with sandbox-first calendar strategy.
| 2025-09-07 | Added repository structure section and updated future enhancements.
| 2025-09-07 | Added repository structure to codebase.

---

## 🔮 Future Enhancements

* Support multiple goal categories (health, work, learning, personal projects).
* Advanced scheduling: priority balancing, adaptive rescheduling, focus-time batching.
* Web dashboard with calendar + goal visualization.
* Multi-user support with role-based access control.
* Plugin system for new integrations (email, task managers, note-taking apps).
* Cross-device sync with optional encrypted cloud backup.
* Mobile app interface for quick goal capture and schedule updates.
* Fine-grained permissions & safety policies for file and calendar operations.
* Experiment with larger or specialized models (e.g., code-focused LLMs, hybrid search).
