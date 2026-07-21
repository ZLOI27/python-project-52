install:
	uv sync

collectstatic:
	:

migrate:
	uv run python manage.py migrate

start:
	uv run python manage.py runserver

lint:
	uv run ruff check

messages:
	uv run python manage.py makemessages -l ru --ignore=.venv/*

compilemessages:
	uv run python manage.py compilemessages --ignore=.venv/*

test:
	uv run python manage.py test

check:
	uv run ruff format --check
	uv run ruff check
	uv run python manage.py check
	uv run python manage.py makemigrations --check --dry-run
	uv run python manage.py test

fix:
	uv run ruff check --fix
	uv run ruff format
	uv run python manage.py makemessages -l ru --ignore=.venv/*
	uv run python manage.py compilemessages --ignore=.venv/*

coverage:
	uv run coverage run manage.py test
	uv run coverage xml

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

.PHONY: install test lint selfcheck check build