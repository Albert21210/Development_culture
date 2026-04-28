# Переменные
VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

# Цвета для вывода
YELLOW := $(shell tput setaf 3)
RESET  := $(shell tput sgr0)

.PHONY: all venv install typecheck lint check-requirements format check run clean

all: check test

# 1. Работа с окружением
$(VENV)/bin/activate: requirements.txt
	@echo "$(YELLOW)Creating virtual environment...$(RESET)"
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate

venv: $(VENV)/bin/activate

install: venv

# 2. Проверка типов
typecheck: venv
	@echo "$(YELLOW)Running type check...$(RESET)"
	$(PYTHON) -m mypy src/

# 3. Проверка стилей (flake8 для проверки, black для форматирования)
lint: venv
	@echo "$(YELLOW)Running linter...$(RESET)"
	$(PYTHON) -m flake8 src/

format: venv
	@echo "$(YELLOW)Formatting code with Black...$(RESET)"
	$(PYTHON) -m black src/

# 4. Проверка зависимостей (pip-extra-reqs или самописный скрипт)
check-requirements: venv
	@echo "$(YELLOW)Checking for missing/extra dependencies...$(RESET)"
	@# Простой способ: проверить, все ли импорты из src доступны в окружении
	$(PYTHON) -m pip_check_reqs --ignore-extra src/

# 5. Цепочки (Композиция)
# Объединяем все проверки качества кода
check: typecheck lint check-requirements
	@echo "$(YELLOW)All checks passed!$(RESET)"

# Запуск приложения в корректном окружении
run: venv
	$(PYTHON) src/app.py

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +