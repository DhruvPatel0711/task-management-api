# Task Management API

> A production-ready RESTful API for task management built with FastAPI, featuring JWT authentication, role-based access control, and full CRUD operations.

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://docker.com)

---

## Features

- **JWT Authentication** — Secure login with OAuth2 password flow and token-based sessions
- **Role-Based Access Control** — Admin and User roles with endpoint-level guards
- **Full Task CRUD** — Create, read, update, and soft-delete tasks with ownership enforcement
- **User Management** — Admin-only user creation, deletion, and restoration
- **Soft Delete** — Non-destructive deletion with restore capability for both users and tasks
- **Async Architecture** — Fully async with SQLAlchemy AsyncSession and asyncpg
- **Database Migrations** — Managed with Alembic for safe schema evolution
- **Docker Deployment** — Single-command deployment with Docker Compose (PostgreSQL + API)
- **Integration Tests** — Comprehensive test suite covering all endpoints

---

## API Endpoints

### Authentication
| Method | Endpoint | Access | Description |
|--------|----------|--------|-------------|
| POST | `/auth/login` | Public | Login and receive JWT token |
| GET | `/auth/me` | Authenticated | Get current user info |

### Users (Admin Only)
| Method | Endpoint | Access | Description |
|--------|----------|--------|-------------|
| POST | `/users/` | Admin | Create a new user |
| DELETE | `/users/{id}` | Admin | Soft-delete a user |
| PATCH | `/users/{id}/restore` | Admin | Restore a deleted user |

### Tasks
| Method | Endpoint | Access | Description |
|--------|----------|--------|-------------|
| POST | `/tasks/` | Authenticated | Create a task |
| GET | `/tasks/` | Authenticated | List own tasks |
| GET | `/tasks/{id}` | Authenticated | Get a specific task |
| PUT | `/tasks/{id}` | Authenticated | Update a task |
| DELETE | `/tasks/{id}` | Authenticated | Soft-delete a task |
| PATCH | `/tasks/{id}/restore` | Admin | Restore a deleted task |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI |
| ORM | SQLAlchemy (Async) |
| Database | PostgreSQL (asyncpg) |
| Auth | JWT (PyJWT) + OAuth2 |
| Passwords | pwdlib (Argon2) |
| Config | pydantic-settings |
| Migrations | Alembic |
| Containers | Docker + Docker Compose |
| Testing | requests (integration) |

---

## Project Structure

```
task-management-api/
├── main.py                 ← FastAPI app entry point
├── config.py               ← Pydantic settings (env vars)
├── database.py             ← Async SQLAlchemy engine + session
├── models.py               ← User & Task ORM models
├── security.py             ← JWT, password hashing, auth guards
├── routers/
│   ├── auth.py             ← Login + /me endpoints
│   ├── users.py            ← User management (admin)
│   └── tasks.py            ← Task CRUD endpoints
├── schemas/
│   ├── user.py             ← User request/response schemas
│   └── task.py             ← Task request/response schemas
├── services/
│   ├── auth_service.py     ← Authentication logic
│   ├── user_service.py     ← User business logic
│   └── task_service.py     ← Task business logic
├── alembic/                ← Database migrations
├── Dockerfile              ← Python 3.12-slim container
├── compose.yaml            ← PostgreSQL + API stack
├── test.py                 ← Integration test suite
└── requirements.txt        ← Python dependencies
```

---

## Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/DhruvPatel0711/task-management-api.git
cd task-management-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your database URL and secret key

# Run migrations
alembic upgrade head

# Start the server
uvicorn main:app --reload
```

### Docker Deployment

```bash
# Start PostgreSQL + API
docker compose up -d

# API is available at http://localhost:8000
# Swagger docs at http://localhost:8000/docs
```

---

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | Async database connection string | `postgresql+asyncpg://user:pass@localhost/dbname` |
| `SECRET_KEY` | JWT signing key | `your-secret-key-here` |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry | `60` |

---

## Running Tests

```bash
# Start the server first, then:
python test.py
```

---

## Connect

| Platform | Link |
|----------|------|
| LinkedIn | [linkedin.com/in/dhruvpatel0711](https://linkedin.com/in/dhruvpatel0711) |
| Portfolio | [dhruvpatel0711.github.io/my-portfolio](https://dhruvpatel0711.github.io/my-portfolio) |
