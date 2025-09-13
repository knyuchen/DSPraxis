#!/usr/bin/env python3
"""
Day 1 Practice - Python Basics
Date: 2025-08-21
Goals: Basic String Manipulation
"""

import argparse


def exercise_1():
    """Exercise 1: Basic String Assignment and Printing"""
    print("=== Exercise 1: Basic String Assignment and Printing ===")
    message = "Hi Python!"
    print(message)
    

def exercise_2():
    """Exercise 2: Variable Reassignment"""
    print("=== Exercise 2: Variable Reassignment ===")
    message = "Hello"
    print(message)
    message = "Hi"
    print(message)


def exercise_3():
    """Exercise 3: F-String Formatting"""
    print("=== Exercise 3: F-String Formatting ===")
    name = "John"
    print(f"Hello, {name}, what a nice day!")

def exercise_4():
    """Exercise 4: String Case Methods"""
    print("=== Exercise 4: String Case Methods ===")
    name = "rCay dwEll"
    print(name)
    print(name.title())
    print(name.upper())
    print(name.lower())

def exercise_5():
    """Exercise 5: String with Quotes"""
    print("=== Exercise 5: String with Quotes ===")
    print("Obi Wan once said, 'I have the high ground!'")

def exercise_6():
    """Exercise 6: F-String with Variables"""
    print("=== Exercise 6: F-String with Variables ===")
    famous_person = "Obi Wan"
    famous_quote = "'I have the high ground!'"
    message = f"{famous_person} once said, {famous_quote}"
    print(message)

def exercise_7():
    """Exercise 7: String Stripping Methods"""
    print("=== Exercise 7: String Stripping Methods ===")
    name = "\tJohn\n"
    name2 = "\t\tJohn\t"
    print(name)
    print(name.lstrip())
    print(name.rstrip())
    print(name.strip())
    print(name2)
    print(name2.lstrip())
    print(name2.rstrip())
    print(name2.strip())

def exercise_8():
    """Exercise 8: String Prefix/Suffix Removal"""
    print("=== Exercise 8: String Prefix/Suffix Removal ===")
    name = "ac.pt.txt"
    print(name.removesuffix(".txt"))
    print(name.removeprefix("ac."))


def main():
    """Main function to run all exercises"""
    parser = argparse.ArgumentParser(description='Day X DSP Practice')
    parser.add_argument('--exercise', type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8], 
                       help='Run specific exercise (1, 2, 3, 4, 5, 6, 7, or 8)')
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
        elif args.exercise == 4:
            exercise_4()
        elif args.exercise == 5:
            exercise_5()
        elif args.exercise == 6:
            exercise_6()
        elif args.exercise == 7:
            exercise_7()
        elif args.exercise == 8:
            exercise_8()
    elif args.all:
        exercise_1()
        exercise_2()
        exercise_3()
        exercise_4()
        exercise_5()
        exercise_6()
        exercise_7()
        exercise_8()
    else:
        # Default: run all exercises
        exercise_1()
        exercise_2()
        exercise_3()
        exercise_4()
        exercise_5()
        exercise_6()
        exercise_7()
        exercise_8()


if __name__ == "__main__":
    main()
