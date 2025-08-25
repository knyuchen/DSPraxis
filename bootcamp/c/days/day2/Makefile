# Makefile for Day 2 DSP Practice
# Date: 2025-08-24

# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -O2 -g -D_GNU_SOURCE
LDFLAGS = -lm

# Target executable
TARGET = main

# Source files
SRCS = main.c
OBJS = $(SRCS:.c=.o)

# Default target
all: $(TARGET)

# Build the executable
$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET) $(LDFLAGS)

# Compile source files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Run the program
run: $(TARGET)
	./$(TARGET)

# Run specific exercise
run1: $(TARGET)
	./$(TARGET) -e 1

run2: $(TARGET)
	./$(TARGET) -e 2

run3: $(TARGET)
	./$(TARGET) -e 3

# Clean build files
clean:
	rm -f $(OBJS) $(TARGET)

# Install dependencies (if needed)
install:
	# Add any installation commands here
	@echo "Dependencies installed (if any)"

# Help target
help:
	@echo "Available targets:"
	@echo "  all     - Build the program"
	@echo "  run     - Build and run all exercises"
	@echo "  run1    - Build and run exercise 1"
	@echo "  run2    - Build and run exercise 2"
	@echo "  run3    - Build and run exercise 3"
	@echo "  clean   - Remove build files"
	@echo "  install - Install dependencies"
	@echo "  help    - Show this help"

.PHONY: all run run1 run2 run3 clean install help
