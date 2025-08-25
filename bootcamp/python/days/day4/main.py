#!/usr/bin/env python3
"""
Day 4 Practice - NumPy Basics
Date: 2025-08-24
Goals: Complete Week 1 Day 4 exercises
"""


import argparse


def exercise_1():
    """Exercise 1: Boolean Comparisons and Logical Operators"""
    print("=== Exercise 1: Boolean Comparisons and Logical Operators ===")
    print('apple' == 'Apple')
    print('apple' != 'Apple')
    print('apple' == 'Apple'.lower())
    print(5>5)
    print(5>=5)
    print(5<5)
    print(5<=5)
    print('apple' in ['apple', 'banana', 'cherry'])
    print('apple' not in ['apple', 'banana', 'cherry'])

def exercise_2():
    """Exercise 2: If-Else Statements and Conditional Logic"""
    print("=== Exercise 2: If-Else Statements and Conditional Logic ===")
    alien_color = 'green'
    if alien_color == 'green':
        print('You just earned 5 points!')
    alien_color = 'red'
    if alien_color == 'green':
        print('You just earned 5 points!')
    else:
        print('You just earned 10 points!')
    alien_color = 'yellow'
    if alien_color == 'green':
        print('You just earned 5 points!')
    elif alien_color == 'yellow':
        print('You just earned 10 points!')
    elif alien_color == 'red':
        print('You just earned 15 points!')

def exercise_3():
    """Exercise 3: If-Elif-Else Chain for Age Classification"""
    print("=== Exercise 3: If-Elif-Else Chain for Age Classification ===")
    age = 20
    if age < 2:
        print('You are a baby!')
    elif age < 4:
        print('You are a toddler!')
    elif age < 13:
        print('You are a kid!')
    elif age < 20:
        print('You are a teenager!')
    elif age < 65:
        print('You are an adult!')
    else:
        print('You are an elder!')
    
def exercise_4():
    """Exercise 4: Conditional Checks with Lists"""
    print("=== Exercise 4: Conditional Checks with Lists ===")
    favorite_fruits = ['apple', 'banana', 'cherry']
    if 'apple' in favorite_fruits:
        print('You really like apples!')
    if 'banana' in favorite_fruits: 
        print('You really like bananas!')
    if 'cherry' in favorite_fruits:
        print('You really like cherries!')
    if 'orange' in favorite_fruits:
        print('You really like oranges!')
    if 'pineapple' in favorite_fruits:
        print('You really like pineapples!')
    if 'strawberry' in favorite_fruits:
        print('You really like strawberries!')
    if 'watermelon' in favorite_fruits:
        print('You really like watermelons!')

def exercise_5():
    """Exercise 5: For Loops with Conditional Logic"""
    print("=== Exercise 5: For Loops with Conditional Logic ===")
    users = ['admin', 'user1', 'user2', 'user3', 'user4']
    if users:
        for user in users:
            if user == 'admin':
                print('Hello admin, would you like to see a status report?')
            else:
                print(f'Hello {user}, thank you for logging in again!')
    else:
        print('We need to find some users!')

def exercise_6():
    """Exercise 6: User Input Validation with Lists"""
    print("=== Exercise 6: User Input Validation with Lists ===")
    current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
    new_users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
    for new_user in new_users:
        if new_user in current_users:
            print(f'{new_user} is already taken. Please enter a new username.')
        else:
            print(f'{new_user} is available.')

def exercise_7():
    """Exercise 7: Conditional Logic with Ordinal Numbers"""
    print("=== Exercise 7: Conditional Logic with Ordinal Numbers ===")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for number in numbers:
        if number == 1:
            print(f'{number}st')
        elif number == 2:
            print(f'{number}nd')
        elif number == 3:
            print(f'{number}rd')
        else:
            print(f'{number}th')

def exercise_8():
    """Exercise 8: Dictionary Creation and Access"""
    print("=== Exercise 8: Dictionary Creation and Access ===")
    random_person = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 25,
        'city': 'New York'
    }
    print(random_person)
    print(random_person['first_name'])
    print(random_person['last_name'])
    print(random_person['age'])
    print(random_person['city'])

def exercise_9():
    """Exercise 9: Dictionary with Multiple Key-Value Pairs"""
    print("=== Exercise 9: Dictionary with Multiple Key-Value Pairs ===")
    favorite_numbers  = {
        'John': 3,
        'Jane': 5,
        'Jim': 7,
        'Jill': 9,
        'Jack': 11
    }
    print(favorite_numbers)
    print(favorite_numbers['John'])
    print(favorite_numbers['Jane'])
    print(favorite_numbers['Jim'])
    print(favorite_numbers['Jill'])
    print(favorite_numbers['Jack'])

def exercise_10():
    """Exercise 10: Dictionary as a Simple Database"""
    print("=== Exercise 10: Dictionary as a Simple Database ===")
    programming_terms = {
        'variable': 'A named storage location in memory that can hold a value',
        'function': 'A block of code that can be called to perform a specific task',
        'loop': 'A control flow statement that allows code to be executed multiple times',
        'list': 'A collection of items that are ordered and mutable',
        'dictionary': 'A collection of key-value pairs that are unordered and mutable'
    }
    print(f'Variable: {programming_terms["variable"]}')
    print(f'Function: {programming_terms["function"]}')
    print(f'Loop: {programming_terms["loop"]}')
    print(f'List: {programming_terms["list"]}')
    print(f'Dictionary: {programming_terms["dictionary"]}')

def main():
    """Main function to run all exercises"""
    parser = argparse.ArgumentParser(description='Day 4 DSP Practice')
    parser.add_argument('--exercise', type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                       help='Run specific exercise (1-10)')
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


if __name__ == "__main__":
    main()
