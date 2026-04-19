PYTHON = python3
VENV = venv
BIN = $(VENV)/bin
PROJECT_DIR = simple_math_flow

.PHONY: all venv install test lint build upload clean

all: venv install lint test

venv:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install twine build pytest ruff mypy

install:
	cd $(PROJECT_DIR) && ../$(BIN)/pip install -e .

test:
	$(BIN)/pytest $(PROJECT_DIR)/tests/

lint:
	$(BIN)/ruff check $(PROJECT_DIR)/src/
	$(BIN)/mypy $(PROJECT_DIR)/src/

build: clean
	cd $(PROJECT_DIR) && ../$(BIN)/python3 -m build

upload:
	$(BIN)/python3 -m twine upload --repository testpypi $(PROJECT_DIR)/dist/*

clean:
	rm -rf $(PROJECT_DIR)/build/ $(PROJECT_DIR)/dist/ $(PROJECT_DIR)/*.egg-info
	find . -name "__pycache__" -exec rm -rf {} +