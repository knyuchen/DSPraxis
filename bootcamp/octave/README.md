# Octave DSP Bootcamp

My structured Octave learning path for DSP applications, organized by weeks and days.

## 📁 Structure

```
bootcamp/octave/
├── template_day/           # Template folder for new days
│   ├── main.m             # Template main.m
│   ├── README.md          # Template README.md
│   ├── data/              # Sample data files
│   ├── output/            # Generated outputs and plots
│   └── scripts/           # Additional script files
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
- `main.m` - Main practice script
- `README.md` - Daily goals and notes
- `data/` - Sample data files (if needed)
- `output/` - Generated plots and results
- `scripts/` - Additional function files

## 🚀 Quick Start

### Setting up a new day:
```bash
# Create a new day (basic)
python3 setup_day.py 1 2

# Create a new day with topic
python3 setup_day.py 1 2 "Signal Analysis"

# Navigate to the new day
cd week1/day2

# Run with Octave
octave main.m
```

### Running exercises:
```bash
# Run main script
octave main.m

# Run Octave interactively
octave

# In Octave, run specific exercises
octave> main
octave> exercise_1
octave> exercise_2
octave> exercise_3
```

## 📚 Weekly Themes

- **Week 1**: Octave Basics & Matrix Operations
- **Week 2**: Signal Processing Toolbox Functions
- **Week 3**: Plotting & Visualization
- **Week 4**: Frequency Domain Analysis
- **Week 5**: Filter Design & Implementation  
- **Week 6**: Advanced DSP Applications

## 📝 Progress Tracking

- [ ] Week 1 Complete
- [ ] Week 2 Complete
- [ ] Week 3 Complete
- [ ] Week 4 Complete
- [ ] Week 5 Complete
- [ ] Week 6 Complete
