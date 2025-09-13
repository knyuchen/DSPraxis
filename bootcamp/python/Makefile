# Makefile for Python DSP Bootcamp
# This Makefile helps with Python environment setup and common tasks

.PHONY: help setup clean install test run-day run-week shell

# Default target
help:
	@echo "Python DSP Bootcamp Makefile"
	@echo "============================"
	@echo ""
	@echo "Available targets:"
	@echo "  setup      - Set up Python virtual environment"
	@echo "  install    - Install Python dependencies"
	@echo "  clean      - Clean Python cache and build files"
	@echo "  test       - Run tests (if any)"
	@echo "  run-day    - Run a specific day (usage: make run-day DAY=2)"
	@echo "  run-all-days - Run all days"
	@echo "  shell      - Activate virtual environment and start Python shell"
	@echo "  help       - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make setup"
	@echo "  make install"
	@echo "  make run-day DAY=1"
	@echo "  make run-all-days"
	@echo "  make shell"

# Set up Python virtual environment
setup:
	@echo "Setting up Python virtual environment..."
	python3 -m venv venv
	@echo "Virtual environment created. Activate it with:"
	@echo "  source venv/bin/activate"

# Install dependencies
install:
	@echo "Installing Python dependencies..."
	@if [ -d "venv" ]; then \
		venv/bin/pip install -r requirements.txt; \
	else \
		echo "Virtual environment not found. Run 'make setup' first."; \
		exit 1; \
	fi

# Clean Python cache and build files
clean:
	@echo "Cleaning Python cache and build files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name "*.pyo" -delete 2>/dev/null || true
	find . -name "*.pyd" -delete 2>/dev/null || true
	find . -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleanup completed."

# Run tests (placeholder for future test framework)
test:
	@echo "Running tests..."
	@echo "No tests configured yet. Add pytest or unittest tests here."

# Run a specific day
run-day:
	@if [ -z "$(DAY)" ]; then \
		echo "Usage: make run-day DAY=<day_number>"; \
		echo "Example: make run-day DAY=2"; \
		exit 1; \
	fi
	@echo "Running Day $(DAY)..."
	@if [ -f "days/day$(DAY)/main.py" ]; then \
		cd days/day$(DAY) && ../../venv/bin/python main.py; \
	else \
		echo "Day $(DAY) not found. Create it first with:"; \
		echo "  python3 setup_day.py 1 $(DAY)"; \
	fi

# Run all days
run-all-days:
	@echo "Running all days..."
	@for day in 1 2 3 4 5 6 7 8 9 10 11 12 13 14; do \
		if [ -f "days/day$$day/main.py" ]; then \
			echo "Running Day $$day..."; \
			cd days/day$$day && ../../venv/bin/python main.py && cd ../..; \
		fi; \
	done

# Activate virtual environment and start Python shell
shell:
	@if [ -d "venv" ]; then \
		echo "Starting Python shell with virtual environment..."; \
		venv/bin/python; \
	else \
		echo "Virtual environment not found. Run 'make setup' first."; \
		exit 1; \
	fi
