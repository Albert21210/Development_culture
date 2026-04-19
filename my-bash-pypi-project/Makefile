PYTHON = python3
VENV = venv
BIN = $(VENV)/bin

.PHONY: all venv install test lint build upload clean

all: venv install lint test build

venv:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install twine build pytest ruff

install:
	$(BIN)/pip install -e .

lint:
	$(BIN)/ruff check src/

test:
	$(BIN)/pytest tests/

build: clean
	$(BIN)/python3 -m build

upload:
	$(BIN)/python3 -m twine upload --repository testpypi dist/*

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache
	find . -name "__pycache__" -exec rm -rf {} +