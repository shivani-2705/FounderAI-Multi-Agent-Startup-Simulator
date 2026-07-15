# 🚀 FounderAI

FounderAI is a local AI-powered multi-agent startup planning platform that transforms a startup idea into a complete business plan using multiple specialized AI agents.

Instead of interacting with a single LLM, FounderAI simulates an executive team consisting of:

- 👨‍💼 CEO
- 👨‍💻 CTO
- 📋 Product Manager
- 🎨 UI/UX Designer
- 📢 Marketing Strategist
- 💰 Investor

Each agent performs its own task, reviews previous work when required, and produces structured outputs that together form a complete startup blueprint.

---

# Features

- Multi-Agent AI Workflow
- Local LLM using Ollama (Qwen 3 8B)
- FastAPI Backend
- React + TypeScript Frontend
- PostgreSQL Persistence
- Workflow Progress Tracking
- Agent Timeline / History
- Structured JSON Responses
- Review & Revision Loop
- Modular Architecture

---

# Architecture

```
                +----------------------+
                |     React Frontend   |
                +----------+-----------+
                           |
                           |
                    REST API
                           |
                           ▼
                 +-------------------+
                 |      FastAPI      |
                 +---------+---------+
                           |
                Startup Orchestrator
                           |
      -----------------------------------------
      |      |      |      |      |          |
     CEO    CTO     PM   Designer Marketing Investor
      |      |      |      |      |          |
      -----------------------------------------
                           |
                      Ollama (Qwen3)
                           |
                     Structured Output
                           |
                     PostgreSQL Database
```

---

# Workflow

```
Idea
  │
  ▼
CEO Analysis
  │
  ▼
CTO Architecture
  │
  ▼
PM Review
  │
Revision Required?
  │
Yes ───────────────► CTO Revision
  │
No
  ▼
PM PRD
  │
  ▼
Designer
  │
  ▼
Marketing
  │
  ▼
Investor
  │
  ▼
Completed
```

---

# Tech Stack

## Backend

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic

## AI

- Ollama
- Qwen3 8B

## Frontend

- React
- TypeScript
- React Router
- Axios

## Database

- PostgreSQL

---

# Folder Structure

```
backend/

app/
 ├── agents/
 ├── orchestrator/
 ├── workflows/
 ├── repositories/
 ├── db/
 ├── memory/
 ├── api/
 ├── schemas/
 ├── services/
 └── main.py

frontend/

src/
 ├── pages/
 ├── components/
 ├── hooks/
 ├── services/
 ├── layouts/
 └── types/
```

---

# Screens

## Home

- Enter startup idea
- Generate project

## Project Dashboard

- Live workflow progress
- Current executing agent
- AI-generated startup documents

## Workflow History

- Timeline of every agent action
- Reviews
- Revisions
- Decisions

---

# Running Locally

## Backend

```bash
cd backend

uv sync

docker compose up -d

uv run alembic upgrade head

ollama serve

ollama pull qwen3:8b

uv run uvicorn app.main:app --reload
```

Backend runs at

```
http://localhost:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# API

## Create Project

```
POST /api/v1/projects
```

---

## Project Status

```
GET /api/v1/projects/{id}/status
```

---

## Project Result

```
GET /api/v1/projects/{id}
```

---

## Workflow History

```
GET /api/v1/projects/{id}/history
```

---

# Future Improvements

- Authentication
- Project Dashboard
- Export as PDF
- Export as Markdown
- WebSocket Live Updates
- Streaming Agent Responses
- Multiple LLM Support
- RAG Knowledge Base
- Docker Deployment
- Cloud Deployment

---

