.PHONY: validate test snapshot all lint format check

validate:
	python scripts/validate_project.py

test:
	cd lri-reference && python -m pytest -q

snapshot:
	python scripts/generate_validation_results.py

lint:
	pip install -q ruff && ruff check .

format:
	pip install -q black && black --check .

check: lint format validate test

all: validate test snapshot
