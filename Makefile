install:
	uv sync

start:
	uv run python manage.py runserver

lint:
	uv run ruff check

fix:
	uv run ruff check --fix

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

.PHONY: install test lint selfcheck check build