.PHONY: test test-cov lint
PY ?= python

test:
	$(PY) -m pytest

test-cov:
	$(PY) -m pytest --cov=app --cov-report=term-missing

