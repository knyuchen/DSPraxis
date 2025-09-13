#!/usr/bin/env python3
"""
Day 5 Practice - Week 1 Day 5 Practice
Date: 2025-08-27
Goals: Complete Week 1 Day 5 exercises
"""


import argparse


def exercise_1():
    """Exercise 1: Dictionary Iteration and Display"""
    print("=== Exercise 1: Dictionary Iteration and Display ===")
    programming_terms = {
        'variable': 'A named storage location in memory that can hold a value',
        'function': 'A block of code that can be called to perform a specific task',
        'loop': 'A control flow statement that allows code to be executed multiple times',
        'list': 'A collection of items that are ordered and mutable',
        'dictionary': 'A collection of key-value pairs that are unordered and mutable'
    }
    for term, definition in programming_terms.items():
        print(f'{term}: {definition}')


def exercise_2():
    """Exercise 2: Dictionary Keys, Values, and Items"""
    print("=== Exercise 2: Dictionary Keys, Values, and Items ===")
    river_origins = {
        'Nile': 'Egypt',
        'Amazon': 'South America',
        'Yangtze': 'China',
        'Mississippi': 'United States',
        'Ganges': 'India'
    }
    for river, origin in river_origins.items():
        print(f'The {river} runs through {origin}')
    for river in river_origins.keys():
        print(f'{river}')
    for origin in river_origins.values():
        print(f'{origin}')


def exercise_3():
    """Exercise 3: Dictionary Membership and Conditional Logic"""
    print("=== Exercise 3: Dictionary Membership and Conditional Logic ===")
    list_of_people = ['John', 'Jane', 'Jim', 'Jill']
    poll_results = {
        'John': 'Python',
        'Jane': 'Java',
        'Jill': 'Python'
    }
    for person in list_of_people:
        if person in poll_results.keys():
            print(f'{person} voted for {poll_results[person]}')
        else:
            print(f'{person} has not voted yet.')

def exercise_4():
    """Exercise 4: List of Dictionaries"""
    print("=== Exercise 4: List of Dictionaries ===")
    jdoe = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 25,
        'city': 'New York'
    }
    ksmith = {
        'first_name': 'Kate',
        'last_name': 'Smith',
        'age': 30,
        'city': 'Los Angeles'
    }
    mjohnson = {
        'first_name': 'Mike',
        'last_name': 'Johnson',
        'age': 35,
        'city': 'Chicago'
    }
    people = [jdoe, ksmith, mjohnson]
    for person in people:
        print(f'{person["first_name"]} {person["last_name"]} is {person["age"]} years old and lives in {person["city"]}')

def exercise_5():
    """Exercise 5: Dictionary with List Values"""
    print("=== Exercise 5: Dictionary with List Values ===")
    favorite_places = {
        'John': ['New York', 'Los Angeles', 'Chicago'],
        'Kate': ['Paris', 'London', 'Berlin'],
        'Mike': ['Tokyo']
    }
    for name, places in favorite_places.items():
        if len(places) == 1:
            print(f'{name}\'s favorite place is:')
        else:
            print(f'{name}\'s favorite places are:')
        for place in places:
            print(f'- {place}')

def exercise_6():
    """Exercise 6: Nested Dictionaries"""
    print("=== Exercise 6: Nested Dictionaries ===")
    cities = {
        'New York': {
            'country': 'United States',
            'population': 8405837,
            'fact': 'New York is the most populous city in the United States'
        },
        'Paris': {
            'country': 'France',
            'population': 2140526,
            'fact': 'Paris is the most populous city in France'
        },
        'Tokyo': {
            'country': 'Japan',
            'population': 37400000,
            'fact': 'Tokyo is the most populous city in Japan'
        }
    }
    for city, info in cities.items():
        print(f'{city} is in {info["country"]}. It has a population of {info["population"]} and a fact: {info["fact"]}')

def exercise_7():
    """Exercise 7: User Input and String Formatting"""
    print("=== Exercise 7: User Input and String Formatting ===")
    print("Simulating user input: 'Tesla'")
    car_input = "Tesla"  # Simulated input for automated testing
    print(f'Let me see if I can find you a {car_input}')

def exercise_8():
    """Exercise 8: Conditional Logic with User Input"""
    print("=== Exercise 8: Conditional Logic with User Input ===")
    print("Simulating user input: 6")
    number_of_people = 6  # Simulated input for automated testing
    if number_of_people > 8:
        print("You'll have to wait for a table.")
    else:
        print("Your table is ready.")

def exercise_9():
    """Exercise 9: Number Validation with Modulo"""
    print("=== Exercise 9: Number Validation with Modulo ===")
    print("Simulating user input: 30")
    number_input = 30  # Simulated input for automated testing
    if number_input % 10 == 0:
        print("The number is a multiple of 10.")
    else:
        print("The number is not a multiple of 10.")

def exercise_10():
    """Exercise 10: While Loop with User Input"""
    print("=== Exercise 10: While Loop with User Input ===")
    print("Simulating pizza toppings: 'pepperoni', 'mushrooms', 'quit'")
    toppings_list = ['pepperoni', 'mushrooms', 'quit']
    for topping in toppings_list:
        if topping == 'quit':
            print("Pizza order complete!")
            break
        else:
            print(f'I\'ll add {topping} to your pizza.')
def exercise_11():
    """Exercise 11: Age-Based Pricing with Conditional Logic"""
    print("=== Exercise 11: Age-Based Pricing with Conditional Logic ===")
    print("Simulating user input: 8")
    age = 8  # Simulated input for automated testing
    if age < 3:
        print("Your ticket is free.")
    elif age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
def exercise_12():
    """Exercise 12: While Loop with List Operations"""
    print("=== Exercise 12: While Loop with List Operations ===")
    sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'turkey', 'ham', 'pastrami']
    finished_sandwiches = []
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print(f'I made your {current_sandwich} sandwich.')
        finished_sandwiches.append(current_sandwich)
    for sandwich in finished_sandwiches:
        print(f'{sandwich} sandwich is ready.')

def exercise_13():
    """Exercise 13: List Filtering with While Loop"""
    print("=== Exercise 13: List Filtering with While Loop ===")
    sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'turkey', 'ham', 'pastrami']
    print(f'I\'m sorry, we\'re out of pastrami.')
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    for sandwich in sandwich_orders:
        print(f'I made your {sandwich} sandwich.')

def exercise_14():
    """Exercise 14: Interactive Poll with Dictionary Storage"""
    print("=== Exercise 14: Interactive Poll with Dictionary Storage ===")
    print("Simulating poll responses:")
    responses = {
        'Alice': 'Paris',
        'Bob': 'Tokyo',
        'Charlie': 'New York'
    }
    for name, response in responses.items():
        print(f'{name} would like to visit {response}.')

def exercise_15():
    """Exercise 15: Advanced Dictionary Operations Summary"""
    print("=== Exercise 15: Advanced Dictionary Operations Summary ===")
    print("Day 5 completed! You've mastered:")
    print("- Dictionary iteration and manipulation")
    print("- User input handling and validation")
    print("- While loops with conditional logic")
    print("- List operations and filtering")
    print("- Complex data structures and nested dictionaries")
def main():
    """Main function to run all exercises"""
    parser = argparse.ArgumentParser(description='Day 5 DSP Practice')
    parser.add_argument('--exercise', type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
                       help='Run specific exercise (1-15)')
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
        elif args.exercise == 9:
            exercise_9()
        elif args.exercise == 10:
            exercise_10()
        elif args.exercise == 11:
            exercise_11()
        elif args.exercise == 12:
            exercise_12()
        elif args.exercise == 13:
            exercise_13()
        elif args.exercise == 14:
            exercise_14()
        elif args.exercise == 15:
            exercise_15()
    elif args.all:
        exercise_1()
        exercise_2()
        exercise_3()
        exercise_4()
        exercise_5()
        exercise_6()
        exercise_7()
        exercise_8()
        exercise_9()
        exercise_10()
        exercise_11()
        exercise_12()
        exercise_13()
        exercise_14()
        exercise_15()
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
        exercise_9()
        exercise_10()
        exercise_11()
        exercise_12()
        exercise_13()
        exercise_14()
        exercise_15()


if __name__ == "__main__":
    main()
