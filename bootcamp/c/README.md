# C DSP Bootcamp

My structured C learning path for DSP applications, organized by weeks and days.

## 📁 Structure

```
bootcamp/c/
├── template_day/           # Template folder for new days
│   ├── main.c             # Template main.c
│   ├── Makefile           # Build configuration
│   ├── README.md          # Template README.md
│   ├── data/              # Sample data files
│   ├── output/            # Generated outputs
│   ├── src/               # Source files
│   └── include/           # Header files
├── setup_day.py           # Script to create new days
├── days/                  # All practice days
│   ├── day1/              # Basic arrays and signals
│   ├── day2/              # Signal processing basics
│   └── ...                # Additional days
└── ...
```

## 🎯 Daily Practice Structure

Each day folder contains:
- `main.c` - Main practice program
- `Makefile` - Build configuration
- `README.md` - Daily goals and notes
- `data/` - Sample data files (if needed)
- `output/` - Generated outputs and results
- `src/` - Additional source files
- `include/` - Header files

## 🚀 Quick Start

### Setting up a new day:
```bash
# Create a new day (basic)
python3 setup_day.py 1 2

# Create a new day with topic
python3 setup_day.py 1 2 "Array Operations"

# Navigate to the new day
cd days/day2

# Build and run
make
./main
```

### Building and running:
```bash
# Build the program
make

# Run the program
./main

# Clean build files
make clean

# Run with specific exercise
./main --exercise 1
```

## 📚 Learning Progression

- **Days 1-3**: C Basics & Memory Management
- **Days 4-7**: Arrays, Pointers & DSP Data Structures
- **Days 8-10**: Functions & Modular Programming
- **Days 11-14**: File I/O & Advanced DSP Algorithms

## 📝 Progress Tracking

- [x] Day 1 Complete (Basic Arrays and Signals)
- [ ] Day 2 (Signal Processing Basics)
- [ ] Day 3 (C Basics)
- [ ] Day 4 (Memory Management)
- [ ] Day 5 (Pointers)
- [ ] Day 6 (DSP Data Structures)
- [ ] Day 7 (Advanced Arrays)
- [ ] Day 8 (Functions)
- [ ] Day 9 (Modular Programming)
- [ ] Day 10 (Function Optimization)
- [ ] Day 11 (File I/O)
- [ ] Day 12 (Data Processing)
- [ ] Day 13 (Real-time Processing)
- [ ] Day 14 (Advanced DSP Algorithms)
