# Task Manager

### Hexlet tests and linter status:
[![Actions Status](https://github.com/ZLOI27/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ZLOI27/python-project-52/actions)

[![CI](https://github.com/ZLOI27/python-project-52/actions/workflows/my-check.yml/badge.svg)](https://github.com/ZLOI27/python-project-52/actions/workflows/my-check.yml)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ZLOI27_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=ZLOI27_python-project-52)

### Link:
[Project on render.com](https://python-project-52-069x.onrender.com/)

[![CI](https://github.com/ZLOI27/python-project-52/actions/workflows/ci.yml/badge.svg)](https://github.com/ZLOI27/python-project-52/actions/workflows/ci.yml)

Task Manager is a web application inspired by Redmine. It allows users to create, edit, assign, filter, and manage tasks. The project was developed as part of the Hexlet Python Backend Developer course.

## Features

- User registration and authentication
- User management (CRUD)
- Status management (CRUD)
- Label management (CRUD)
- Task management (CRUD)
- Task filtering by:
  - Status
  - Executor
  - Label
  - Own tasks only
- Internationalization (English and Russian)
- Error monitoring with Rollbar

## Tech Stack

- Python 3.13
- Django 6
- PostgreSQL / SQLite
- Bootstrap 5
- django-filter
- uv
- Ruff
- GitHub Actions
- Rollbar

## Installation

Clone the repository:

```bash
git clone https://github.com/ZLOI27/python-project-52.git
cd python-project-52
```

Install dependencies:

```bash
make install
```

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url

ROLLBAR_ACCESS_TOKEN=your_rollbar_token
# development | production
ROLLBAR_ENVIRONMENT=development
```

Apply migrations:

```bash
make migrate
```

Run the development server:

```bash
make start
```

The application will be available at:

```
http://127.0.0.1:8000
```

## Testing and Code Quality

Run all project checks:

```bash
make check
```

Or run them separately:

```bash
make lint
make test
```

