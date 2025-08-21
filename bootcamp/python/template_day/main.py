#!/usr/bin/env python3
"""
Day X Practice - [Topic]
Date: [Date]
Goals: [List of goals for this day]
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import argparse


def exercise_1():
    """Exercise 1: [Description]"""
    print("=== Exercise 1: [Description] ===")
    # Your code here
    pass


def exercise_2():
    """Exercise 2: [Description]"""
    print("=== Exercise 2: [Description] ===")
    # Your code here
    pass


def exercise_3():
    """Exercise 3: [Description]"""
    print("=== Exercise 3: [Description] ===")
    # Your code here
    pass


def main():
    """Main function to run all exercises"""
    parser = argparse.ArgumentParser(description='Day X DSP Practice')
    parser.add_argument('--exercise', type=int, choices=[1, 2, 3], 
                       help='Run specific exercise (1, 2, or 3)')
    parser.add_argument('--all', action='store_true', 
                       help='Run all exercises')
    
    args = parser.parse_args()
    
    if args.exercise:
        if args.exercise == 1:
            exercise_1()
        elif args.exercise == 2:
            exercise_2()
        elif args.exercise == 3:
            exercise_3()
    elif args.all:
        exercise_1()
        exercise_2()
        exercise_3()
    else:
        # Default: run all exercises
        exercise_1()
        exercise_2()
        exercise_3()


if __name__ == "__main__":
    main()
