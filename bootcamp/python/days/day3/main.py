#!/usr/bin/env python3
"""
Day 3 Practice - [Topic]
Date: 2025-08-23
Goals: [List of goals for this day]
"""


import argparse


def exercise_1():
    """Exercise 1: For Loops and List Copying"""
    print("=== Exercise 1: For Loops and List Copying ===")
    flavors_of_pizza = ["pepperoni", "cheese", "margherita", "hawaiian"]
    for flavor in flavors_of_pizza:
        print(f"I like {flavor} pizza")
    print("I really love pizza!")
    friend_pizzas = flavors_of_pizza[:]
    flavors_of_pizza.append("apple")
    friend_pizzas.append("veggie")
    for flavor in flavors_of_pizza:
        print(f"My favorite pizzas are: {flavor}")
    for flavor in friend_pizzas:
        print(f"My friend's favorite pizzas are: {flavor}")

def exercise_2():
    """Exercise 2: For Loops and List Slicing"""
    print("=== Exercise 2: For Loops and List Slicing ===")
    animals_for_pets = ["dog", "cat", "fish", "bird", "rabbit"]
    for animal in animals_for_pets:
        print(f"A {animal} would make a great pet")
    print("Any of these animals would make a great pet!")
    print(f"The first three items in the list are: {animals_for_pets[:3]}")
    print(f"Three items from the middle of the list are: {animals_for_pets[2:5]}")
    print(f"The last three items in the list are: {animals_for_pets[-3:]}")

def exercise_3():
    """Exercise 3: List Comprehensions and Range Operations"""
    print("=== Exercise 3: List Comprehensions and Range Operations ===")
    print([i for i in range(1, 21)])
    million_num = [i for i in range(1, 1000001)]
    print(min(million_num))
    print(max(million_num))
    print(sum(million_num))
    print([i for i in range(1, 21, 2)])
    print([i for i in range(3, 31, 3)])
    print([i**3 for i in range(1, 11)])

def exercise_4():
    """Exercise 4: Tuples and Immutability"""
    print("=== Exercise 4: Tuples and Immutability ===")
    simple_food = ("pizza", "burger", "salad", "soup", "pasta")
    for food in simple_food:
        print(food)
    simple_food = ("pizza", "chicken", "rice", "soup", "pasta")
    for food in simple_food:
        print(food)

def main():
    """Main function to run all exercises"""
    parser = argparse.ArgumentParser(description='Day X DSP Practice')
    parser.add_argument('--exercise', type=int, choices=[1, 2, 3, 4], 
                       help='Run specific exercise (1, 2, 3, or 4)')
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
    elif args.all:
        exercise_1()
        exercise_2()
        exercise_3()
        exercise_4()
    else:
        # Default: run all exercises
        exercise_1()
        exercise_2()
        exercise_3()
        exercise_4()


if __name__ == "__main__":
    main()
