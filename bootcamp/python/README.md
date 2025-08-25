# Python DSP Bootcamp

My structured Python learning path for DSP applications, organized by weeks and days.

## 📁 Structure

```
bootcamp/python/
├── template_day/           # Template folder for new days
│   ├── main.py            # Template main.py
│   ├── README.md          # Template README.md
│   ├── data/              # Sample data folder
│   └── output/            # Output folder
├── setup_day.py           # Script to create new days
├── days/                  # All practice days
│   ├── day1/              # String basics
│   ├── day2/              # Numbers and lists
│   ├── day3/              # Loops and comprehensions
│   └── ...                # Additional days
└── ...
```

## 🎯 Daily Practice Structure

Each day folder contains:
- `main.py` - Main practice script
- `README.md` - Daily goals and notes
- `data/` - Sample data files (if needed)
- `output/` - Generated outputs and plots

## 🚀 Quick Start

### Setting up a new day:
```bash
# Create a new day (basic)
python3 setup_day.py 1 4

# Create a new day with topic
python3 setup_day.py 1 4 "NumPy Arrays"

# Navigate to the new day
cd days/day4

# Run the day's practice
python main.py
```

### Running exercises:
```bash
# Run all exercises
python main.py

# Run specific exercise
python main.py --exercise 1

# Run all exercises explicitly
python main.py --all
```

## 📚 Learning Progression

- **Days 1-3**: Python Basics (Strings, Numbers, Lists, Loops)
- **Days 4-7**: NumPy Fundamentals & Array Operations
- **Days 8-10**: SciPy & Signal Processing Basics
- **Days 11-14**: Matplotlib & Advanced DSP Applications

## 📝 Progress Tracking

- [x] Day 1 Complete (String Basics)
- [x] Day 2 Complete (Numbers and Lists)
- [x] Day 3 Complete (Loops and Comprehensions)
- [x] Day 4 Complete (Conditionals and Dictionaries)
- [ ] Day 5 (NumPy Arrays)
- [ ] Day 6 (NumPy Operations)
- [ ] Day 7 (NumPy Advanced)
- [ ] Day 8 (SciPy Basics)
- [ ] Day 9 (Signal Processing)
- [ ] Day 10 (SciPy Advanced)
- [ ] Day 11 (Matplotlib Basics)
- [ ] Day 12 (Plotting Signals)
- [ ] Day 13 (Advanced Visualization)
- [ ] Day 14 (DSP Integration)
