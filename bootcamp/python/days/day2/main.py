#!/usr/bin/env python3
"""
Day 2 Practice - [Topic]
Date: 2025-08-22
Goals: [Numbers and Lists]
"""


import argparse


def exercise_1():
    """Exercise 1: Basic Arithmetic Operations"""
    print("=== Exercise 1: Basic Arithmetic Operations ===")
    print(5+3)
    print(10-2)
    print(2*4)
    print(256/32)


def exercise_2():
    """Exercise 2: Constants and F-String with Numbers"""
    print("=== Exercise 2: Constants and F-String with Numbers ===")
    FAVORITE_NUMBER = 25
    print(f"My favorite number is {FAVORITE_NUMBER}")


def exercise_3():
    """Exercise 3: List Creation and Indexing"""
    print("=== Exercise 3: List Creation and Indexing ===")
    names = ["John", "Jane", "Jim", "Jill"]
    print(names)
    print(names[0])
    print(names[1])
    print(names[2])
    print(names[3])

def exercise_4():
    """Exercise 4: List Elements in F-Strings"""
    print("=== Exercise 4: List Elements in F-Strings ===")
    names = ["John", "Jane", "Jim", "Jill"]
    print(f"Hello, {names[0]}!")
    print(f"Hi, {names[1]}!")
    print(f"Hey, {names[2]}!")
    print(f"Ciao, {names[3]}!")

def exercise_5():
    """Exercise 5: List Modification and Guest Management"""
    print("=== Exercise 5: List Modification and Guest Management ===")
    names = ["John", "Jane", "Jim", "Jill"]
    print (f"Hello, {names[0]}!")
    print (f"Hi, {names[1]}!")
    print (f"Hey, {names[2]}!")
    print (f"Ciao, {names[3]}!")
    guest_no_show = names[2]
    print (f"{guest_no_show} can't make it to the party.")
    names[2] = "Jack"
    print (f"Hello, {names[0]}!")
    print (f"Hi, {names[1]}!")
    print (f"Hey, {names[2]}!")
    print (f"Ciao, {names[3]}!")
    print("I found a bigger table!")
    names.insert(0, "Alice")
    names.insert(3, "Bob")
    names.append("Charlie")
    print (f"Hello, {names[0]}!")
    print (f"Hi, {names[1]}!")
    print (f"Hey, {names[2]}!")
    print (f"Ciao, {names[3]}!")
    print (f"Hola, {names[4]}!")
    print (f"Bonjour, {names[5]}!")
    print (f"Hehe, {names[6]}!")
    print ("Now I can only have 2 guests")
    cant_come = names.pop()
    print (f"{cant_come} can't come to the party.")
    cant_come = names.pop()
    print (f"{cant_come} can't come to the party.")
    cant_come = names.pop()
    print (f"{cant_come} can't come to the party.")
    cant_come = names.pop()
    print (f"{cant_come} can't come to the party.")
    cant_come = names.pop()
    print (f"{cant_come} can't come to the party.")
    print (f"Hello, {names[0]}!")
    print (f"Hi, {names[1]}!")
    del names[0]
    del names[0]
    print (names)

def exercise_6():
    """Exercise 6: List Sorting and Ordering Methods"""
    print("=== Exercise 6: List Sorting and Ordering Methods ===")
    places = ["Japan", "Italy", "France", "Germany", "Spain"]
    print (places)
    print (sorted(places))
    print (places)
    print (sorted(places, reverse=True))
    print (places)
    places.reverse()
    print (places)
    places.reverse()
    print (places)
    places.sort()
    print (places)
    places.sort(reverse=True)
    print (places)

def main():
    """Main function to run all exercises"""
    parser = argparse.ArgumentParser(description='Day X DSP Practice')
    parser.add_argument('--exercise', type=int, choices=[1, 2, 3, 4, 5, 6], 
                       help='Run specific exercise (1, 2, 3, 4, 5, or 6)')
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
    elif args.all:
        exercise_1()
        exercise_2()
        exercise_3()
        exercise_4()
        exercise_5()
        exercise_6()
    else:
        # Default: run all exercises
        exercise_1()
        exercise_2()
        exercise_3()
        exercise_4()
        exercise_5()
        exercise_6()

if __name__ == "__main__":
    main()
