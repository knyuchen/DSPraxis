# FPGA Project Makefile
# Easily configurable for different projects

# Project Configuration - Edit these for each new project
PROJECT_NAME = switch_leds
TOP_MODULE = Switches_To_LEDs
SOURCE_FILES = Switches_To_LEDs.v
CONSTRAINT_FILE = ../Go_Board_Constraints.pcf

# Device Configuration
DEVICE = hx1k
PACKAGE = vq100

# Tool Configuration
YOSYS = yosys
NEXTPNR = nextpnr-ice40
ICEPACK = icepack
ICEPROG = iceprog

# Generated file names
JSON_FILE = $(PROJECT_NAME).json
ASC_FILE = $(PROJECT_NAME).asc
BIN_FILE = $(PROJECT_NAME).bin

# Default target
all: $(BIN_FILE)

# Synthesis: Verilog -> JSON
$(JSON_FILE): $(SOURCE_FILES)
	$(YOSYS) -q -p "synth_ice40 -top $(TOP_MODULE) -json $(JSON_FILE)" $(SOURCE_FILES)

# Place & Route: JSON -> ASC
$(ASC_FILE): $(JSON_FILE) $(CONSTRAINT_FILE)
	$(NEXTPNR) --$(DEVICE) --package $(PACKAGE) \
	  --json $(JSON_FILE) --pcf $(CONSTRAINT_FILE) \
	  --pcf-allow-unconstrained --asc $(ASC_FILE)

# Bitstream Generation: ASC -> BIN
$(BIN_FILE): $(ASC_FILE)
	$(ICEPACK) $(ASC_FILE) $(BIN_FILE)

# Program the FPGA
program: $(BIN_FILE)
	$(ICEPROG) $(BIN_FILE)

# Individual targets for debugging
synth: $(JSON_FILE)
place: $(ASC_FILE)
bitstream: $(BIN_FILE)

# Clean up generated files
clean:
	rm -f $(JSON_FILE) $(ASC_FILE) $(BIN_FILE)

# Show help
help:
	@echo "Available targets:"
	@echo "  all        - Build complete bitstream (default)"
	@echo "  synth      - Run synthesis only"
	@echo "  place      - Run place & route only"
	@echo "  bitstream  - Generate bitstream only"
	@echo "  program    - Program the FPGA"
	@echo "  clean      - Remove generated files"
	@echo "  help       - Show this help message"
	@echo ""
	@echo "Configuration:"
	@echo "  PROJECT_NAME = $(PROJECT_NAME)"
	@echo "  TOP_MODULE   = $(TOP_MODULE)"
	@echo "  DEVICE       = $(DEVICE)"
	@echo "  PACKAGE      = $(PACKAGE)"

.PHONY: all synth place bitstream program clean help
