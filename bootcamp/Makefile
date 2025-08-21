# Master Makefile for DSP Praxis Bootcamp
# This Makefile coordinates all three bootcamp sections (Python, C, Octave)

.PHONY: help setup clean run-day run-week run-all status

# Default target
help:
	@echo "DSP Praxis Bootcamp Master Makefile"
	@echo "==================================="
	@echo ""
	@echo "Available targets:"
	@echo "  setup      - Set up all bootcamp environments"
	@echo "  clean      - Clean all build artifacts and cache files"
	@echo "  run-day    - Run a specific day in all languages"
	@echo "  run-week   - Run all days in a week for all languages"
	@echo "  run-all    - Run all existing days in all languages"
	@echo "  status     - Show status of all bootcamp sections"
	@echo "  help       - Show this help message"
	@echo ""
	@echo "Language-specific targets:"
	@echo "  python-setup    - Set up Python environment"
	@echo "  python-clean    - Clean Python cache"
	@echo "  python-run-day  - Run Python day (WEEK=1 DAY=2)"
	@echo "  c-clean         - Clean C build artifacts"
	@echo "  c-run-day       - Run C day (WEEK=1 DAY=2)"
	@echo "  octave-clean    - Clean Octave workspace"
	@echo "  octave-run-day  - Run Octave day (WEEK=1 DAY=2)"
	@echo ""
	@echo "Examples:"
	@echo "  make setup"
	@echo "  make run-day WEEK=1 DAY=1"
	@echo "  make run-week WEEK=2"
	@echo "  make python-run-day WEEK=1 DAY=2"

# Set up all bootcamp environments
setup:
	@echo "Setting up all bootcamp environments..."
	@echo "Setting up Python environment..."
	@cd python && make setup
	@echo "Setting up Python dependencies..."
	@cd python && make install
	@echo "All environments set up successfully!"

# Clean all build artifacts and cache files
clean:
	@echo "Cleaning all bootcamp sections..."
	@cd python && make clean
	@cd c && make clean
	@cd octave && make clean
	@echo "All cleanup completed."

# Run a specific day in all languages
run-day:
	@if [ -z "$(WEEK)" ] || [ -z "$(DAY)" ]; then \
		echo "Usage: make run-day WEEK=<week_number> DAY=<day_number>"; \
		echo "Example: make run-day WEEK=1 DAY=2"; \
		exit 1; \
	fi
	@echo "Running Week $(WEEK) Day $(DAY) in all languages..."
	@echo "=== Python ==="
	@cd python && make run-day WEEK=$(WEEK) DAY=$(DAY) || echo "Python day not found or failed"
	@echo "=== C ==="
	@cd c && make run-day WEEK=$(WEEK) DAY=$(DAY) || echo "C day not found or failed"
	@echo "=== Octave ==="
	@cd octave && make run-day WEEK=$(WEEK) DAY=$(DAY) || echo "Octave day not found or failed"

# Run all days in a week for all languages
run-week:
	@if [ -z "$(WEEK)" ]; then \
		echo "Usage: make run-week WEEK=<week_number>"; \
		echo "Example: make run-week WEEK=1"; \
		exit 1; \
	fi
	@echo "Running Week $(WEEK) in all languages..."
	@echo "=== Python ==="
	@cd python && make run-week WEEK=$(WEEK) || echo "Python week not found or failed"
	@echo "=== C ==="
	@cd c && make run-week WEEK=$(WEEK) || echo "C week not found or failed"
	@echo "=== Octave ==="
	@cd octave && make run-week WEEK=$(WEEK) || echo "Octave week not found or failed"

# Run all existing days in all languages
run-all:
	@echo "Running all existing days in all languages..."
	@echo "=== Python ==="
	@cd python && make run-all || echo "Python run-all failed"
	@echo "=== C ==="
	@cd c && make build-all || echo "C build-all failed"
	@echo "=== Octave ==="
	@cd octave && make run-all || echo "Octave run-all failed"

# Show status of all bootcamp sections
status:
	@echo "DSP Praxis Bootcamp Status"
	@echo "========================="
	@echo ""
	@echo "Python Bootcamp:"
	@cd python && find . -name "main.py" | wc -l | xargs echo "  Days created:"
	@echo "  Virtual environment: $(shell if [ -d "python/venv" ]; then echo "✓ Created"; else echo "✗ Not created"; fi)"
	@echo ""
	@echo "C Bootcamp:"
	@cd c && find . -name "main.c" | wc -l | xargs echo "  Days created:"
	@echo ""
	@echo "Octave Bootcamp:"
	@cd octave && find . -name "main.m" | wc -l | xargs echo "  Days created:"

# Language-specific targets
python-setup:
	@cd python && make setup

python-clean:
	@cd python && make clean

python-run-day:
	@if [ -z "$(WEEK)" ] || [ -z "$(DAY)" ]; then \
		echo "Usage: make python-run-day WEEK=<week_number> DAY=<day_number>"; \
		exit 1; \
	fi
	@cd python && make run-day WEEK=$(WEEK) DAY=$(DAY)

c-clean:
	@cd c && make clean

c-run-day:
	@if [ -z "$(WEEK)" ] || [ -z "$(DAY)" ]; then \
		echo "Usage: make c-run-day WEEK=<week_number> DAY=<day_number>"; \
		exit 1; \
	fi
	@cd c && make run-day WEEK=$(WEEK) DAY=$(DAY)

octave-clean:
	@cd octave && make clean

octave-run-day:
	@if [ -z "$(WEEK)" ] || [ -z "$(DAY)" ]; then \
		echo "Usage: make octave-run-day WEEK=<week_number> DAY=<day_number>"; \
		exit 1; \
	fi
	@cd octave && make run-day WEEK=$(WEEK) DAY=$(DAY)
