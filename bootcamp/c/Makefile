# Makefile for C DSP Bootcamp
# This Makefile helps with C compilation and common tasks

.PHONY: help clean run-day run-week build-all

# Default target
help:
	@echo "C DSP Bootcamp Makefile"
	@echo "======================="
	@echo ""
	@echo "Available targets:"
	@echo "  clean      - Clean all build artifacts"
	@echo "  run-day    - Build and run a specific day (usage: make run-day DAY=2)"
	@echo "  run-all-days - Build and run all days"
	@echo "  build-all  - Build all existing days"
	@echo "  help       - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make run-day DAY=1"
	@echo "  make run-all-days"
	@echo "  make build-all"

# Clean all build artifacts
clean:
	@echo "Cleaning C build artifacts..."
	find . -name "*.o" -delete 2>/dev/null || true
	find . -name "main" -delete 2>/dev/null || true
	find . -name "*.exe" -delete 2>/dev/null || true
	find . -name "*.out" -delete 2>/dev/null || true
	@echo "Cleanup completed."

# Build and run a specific day
run-day:
	@if [ -z "$(DAY)" ]; then \
		echo "Usage: make run-day DAY=<day_number>"; \
		echo "Example: make run-day DAY=2"; \
		exit 1; \
	fi
	@echo "Building and running Day $(DAY)..."
	@if [ -f "days/day$(DAY)/main.c" ]; then \
		cd days/day$(DAY) && make clean && make && ./main; \
	else \
		echo "Day $(DAY) not found. Create it first with:"; \
		echo "  python3 setup_day.py 1 $(DAY)"; \
	fi

# Build and run all days
run-all-days:
	@echo "Building and running all days..."
	@for day in 1 2 3 4 5 6 7 8 9 10 11 12 13 14; do \
		if [ -f "days/day$$day/main.c" ]; then \
			echo "Building and running Day $$day..."; \
			cd days/day$$day && make clean && make && ./main && cd ../..; \
		fi; \
	done

# Build all existing days
build-all:
	@echo "Building all existing C days..."
	@for week in 1 2 3 4 5 6; do \
		for day in 1 2 3 4 5 6 7; do \
			if [ -f "week$$week/day$$day/main.c" ]; then \
				echo "Building Week $$week Day $$day..."; \
				cd week$$week/day$$day && make clean && make && cd ../../; \
			fi; \
		done; \
	done
	@echo "All builds completed."
