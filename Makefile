install:
	uv sync

lint:
	uv run ruff check

fix:
	uv run ruff check --fix

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

.PHONY: install test lint selfcheck check build