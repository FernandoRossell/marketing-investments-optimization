.PHONY: lint format test test-unit test-integration run-api

lint:
	ruff check .

format:
	black .

test:
	pytest -q

test-unit:
	pytest -q tests/unit

test-integration:
	pytest -q tests/integration

run-api:
	uvicorn api.app:app --reload --host 0.0.0.0 --port 8000
