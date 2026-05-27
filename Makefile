.PHONY: validate test snapshot all

validate:
	python scripts/validate_project.py

test:
	cd lri-reference && python -m pytest -q

snapshot:
	python scripts/generate_validation_results.py

all: validate test snapshot
