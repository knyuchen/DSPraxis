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
├── week1/
│   ├── day1/
│   ├── day2/
│   └── ...
├── week2/
│   ├── day1/
│   ├── day2/
│   └── ...
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
cd week1/day2

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

## 📚 Weekly Themes

- **Week 1**: C Basics & Memory Management
- **Week 2**: Arrays, Pointers & DSP Data Structures
- **Week 3**: Functions & Modular Programming
- **Week 4**: File I/O & Data Processing
- **Week 5**: Real-time Processing & Optimization
- **Week 6**: Advanced DSP Algorithms

## 📝 Progress Tracking

- [ ] Week 1 Complete
- [ ] Week 2 Complete
- [ ] Week 3 Complete
- [ ] Week 4 Complete
- [ ] Week 5 Complete
- [ ] Week 6 Complete
