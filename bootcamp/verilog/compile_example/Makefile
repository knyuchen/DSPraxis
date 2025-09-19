# Verilog Simulation Makefile
# Uses Icarus Verilog for compilation and simulation

# Variables
TOP_MODULE = test_counter
SOURCES = counter.sv test_counter.sv
EXECUTABLE = $(TOP_MODULE).out
VCD_FILE = counter.vcd

# Compiler and simulator
IVERILOG = iverilog
VVP = vvp
GTKWAVE = gtkwave

# Default target
all: compile run

# Compile Verilog sources
compile:
	$(IVERILOG) -o $(EXECUTABLE) $(SOURCES)

# Run simulation
run: compile
	$(VVP) $(EXECUTABLE)

# View waveforms in GTKWave
wave: run
	$(GTKWAVE) $(VCD_FILE) &

# Clean generated files
clean:
	rm -f $(EXECUTABLE) $(VCD_FILE)

# Force recompilation
rebuild: clean compile

# Run simulation and show output
sim: run
	@echo "Simulation completed. VCD file: $(VCD_FILE)"

# Help target
help:
	@echo "Available targets:"
	@echo "  all      - Compile and run simulation (default)"
	@echo "  compile  - Compile Verilog sources"
	@echo "  run      - Run simulation"
	@echo "  wave     - Run simulation and open GTKWave"
	@echo "  sim      - Run simulation and show completion message"
	@echo "  clean    - Remove generated files"
	@echo "  rebuild  - Clean and recompile"
	@echo "  help     - Show this help message"

# Phony targets
.PHONY: all compile run wave clean rebuild sim help
