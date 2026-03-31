.PHONY: all install lint test build upload clean

install:
	pip install --upgrade pip
	pip install build twine flake8 mypy pytest
	pip install -r requirements.txt

lint:
	flake8 src/
	mypy src/

test:
	pytest tests/

build: clean
	python3 -m build

upload:
	python3 -m twine upload --repository testpypi dist/*

clean:
	rm -rf dist/ build/ *.egg-info