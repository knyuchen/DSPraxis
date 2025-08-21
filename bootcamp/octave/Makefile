# Makefile for Octave DSP Bootcamp
# This Makefile helps with Octave execution and common tasks

.PHONY: help clean run-day run-week run-all

# Default target
help:
	@echo "Octave DSP Bootcamp Makefile"
	@echo "============================"
	@echo ""
	@echo "Available targets:"
	@echo "  clean      - Clean Octave workspace files"
	@echo "  run-day    - Run a specific day (usage: make run-day WEEK=1 DAY=2)"
	@echo "  run-week   - Run all days in a week (usage: make run-week WEEK=1)"
	@echo "  run-all    - Run all existing days"
	@echo "  help       - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make run-day WEEK=1 DAY=1"
	@echo "  make run-week WEEK=2"
	@echo "  make run-all"

# Clean Octave workspace files
clean:
	@echo "Cleaning Octave workspace files..."
	find . -name "octave-workspace" -delete 2>/dev/null || true
	find . -name "octave-core" -delete 2>/dev/null || true
	find . -name "*.oct" -delete 2>/dev/null || true
	find . -name "*.mex" -delete 2>/dev/null || true
	@echo "Cleanup completed."

# Run a specific day
run-day:
	@if [ -z "$(WEEK)" ] || [ -z "$(DAY)" ]; then \
		echo "Usage: make run-day WEEK=<week_number> DAY=<day_number>"; \
		echo "Example: make run-day WEEK=1 DAY=2"; \
		exit 1; \
	fi
	@echo "Running Week $(WEEK) Day $(DAY)..."
	@if [ -f "week$(WEEK)/day$(DAY)/main.m" ]; then \
		cd week$(WEEK)/day$(DAY) && octave --no-gui main.m; \
	else \
		echo "Day $(WEEK)/$(DAY) not found. Create it first with:"; \
		echo "  python3 setup_day.py $(WEEK) $(DAY)"; \
	fi

# Run all days in a week
run-week:
	@if [ -z "$(WEEK)" ]; then \
		echo "Usage: make run-week WEEK=<week_number>"; \
		echo "Example: make run-week WEEK=1"; \
		exit 1; \
	fi
	@echo "Running all days in Week $(WEEK)..."
	@for day in 1 2 3 4 5 6 7; do \
		if [ -f "week$(WEEK)/day$$day/main.m" ]; then \
			echo "Running Day $$day..."; \
			cd week$(WEEK)/day$$day && octave --no-gui main.m && cd ../..; \
		fi; \
	done

# Run all existing days
run-all:
	@echo "Running all existing Octave days..."
	@for week in 1 2 3 4 5 6; do \
		for day in 1 2 3 4 5 6 7; do \
			if [ -f "week$$week/day$$day/main.m" ]; then \
				echo "Running Week $$week Day $$day..."; \
				cd week$$week/day$$day && octave --no-gui main.m && cd ../../; \
			fi; \
		done; \
	done
	@echo "All runs completed."
