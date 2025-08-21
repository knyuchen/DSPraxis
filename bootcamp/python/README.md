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
- `main.py` - Main practice script
- `README.md` - Daily goals and notes
- `data/` - Sample data files (if needed)
- `output/` - Generated outputs and plots

## 🚀 Quick Start

### Setting up a new day:
```bash
# Create a new day (basic)
python setup_day.py 1 2

# Create a new day with topic
python setup_day.py 1 2 "NumPy Arrays"

# Navigate to the new day
cd week1/day2

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

## 📚 Weekly Themes

- **Week 1**: Python Basics & NumPy Fundamentals
- **Week 2**: SciPy & Signal Processing Basics
- **Week 3**: Matplotlib & Visualization
- **Week 4**: Advanced NumPy & Array Operations
- **Week 5**: Real-world DSP Applications
- **Week 6**: Integration & Project Work

## 📝 Progress Tracking

- [ ] Week 1 Complete
- [ ] Week 2 Complete
- [ ] Week 3 Complete
- [ ] Week 4 Complete
- [ ] Week 5 Complete
- [ ] Week 6 Complete
