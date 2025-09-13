#!/usr/bin/env python3
"""
Day 7 Practice - Day 7 Practice
Date: 2025-08-29
Goals: Complete Day 7 exercises
"""


import argparse
from random import randint, choice

class restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The restaurant is {self.name} and the cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"The restaurant {self.name} is open.")
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, increment):
        self.number_served += increment

def exercise_1():
    """Exercise 1: Basic Class Definition and Methods"""
    print("=== Exercise 1: Basic Class Definition and Methods ===")
    restaurant1 = restaurant("The Restaurant", "Italian")
    print(restaurant1.name)
    print(restaurant1.cuisine_type)
    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()
    restaurant2 = restaurant("The Restaurant 2", "Mexican")
    print(restaurant2.name)
    print(restaurant2.cuisine_type)
    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()
    restaurant3 = restaurant("The Restaurant 3", "Japanese")
    print(restaurant3.name)
    print(restaurant3.cuisine_type)
    restaurant3.describe_restaurant()
    restaurant3.open_restaurant()
    print(restaurant3.number_served)
    restaurant3.set_number_served(10)
    print(restaurant3.number_served)
    restaurant3.increment_number_served(5)
    print(restaurant3.number_served)

class user:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"The user is {self.first_name} {self.last_name} and the age is {self.age} and the location is {self.location}.")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

def exercise_2():
    """Exercise 2: Class Attributes and Method Implementation"""
    print("=== Exercise 2: Class Attributes and Method Implementation ===")
    user1 = user("John", "Doe", 25, "New York")
    user1.describe_user()
    user1.greet_user()
    user2 = user("Jane", "Smith", 30, "Los Angeles")
    user2.describe_user()
    user2.greet_user()
    user3 = user("Jim", "Beam", 35, "Chicago")
    user3.describe_user()
    user3.greet_user()
    user3.increment_login_attempts()
    print(user3.login_attempts)
    user3.reset_login_attempts()
    print(user3.login_attempts)

class ice_cream_stand(restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry"]
    
    def display_flavors(self):
        print(f"The flavors are {self.flavors}.")

def exercise_3():
    """Exercise 3: Class Inheritance and Method Override"""
    print("=== Exercise 3: Class Inheritance and Method Override ===")
    ice_cream_stand1 = ice_cream_stand("The Ice Cream Stand", "Ice Cream")
    ice_cream_stand1.display_flavors()

class privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"The privileges are {self.privileges}.")

class admin(user):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = privileges(["can add post", "can delete post", "can ban user"])
    
    def show_privileges(self):
        print(f"The privileges are {self.privileges}.")

def exercise_4():
    """Exercise 4: Composition and Complex Class Relationships"""
    print("=== Exercise 4: Composition and Complex Class Relationships ===")
    admin1 = admin("John", "Doe", 25, "New York")
    admin1.show_privileges()

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
        return randint(1, self.sides)

def exercise_5():
    """Exercise 5: Random Number Generation and Class Methods"""
    print("=== Exercise 5: Random Number Generation and Class Methods ===")
    dice1 = Dice()
    for i in range(10):
        print(dice1.roll_dice())
    dice2 = Dice(10)
    for i in range(10):
        print(dice2.roll_dice())
    dice3 = Dice(20)
    for i in range(10):
        print(dice3.roll_dice())

def lottery_ticket(total_ticket, ticket_length):
    winning_ticket = []
    for i in range(ticket_length):
        winning_number = choice(total_ticket)
        winning_ticket.append(winning_number)
        total_ticket.remove(winning_number)
    return winning_ticket
def check_ticket(winning_ticket, ticket, ticket_length):
    match = 0
    for number in ticket:
        if number in winning_ticket:
            match += 1
    return match == ticket_length
def exercise_6():
    """Exercise 6: Complex Algorithm Implementation with Classes"""
    print("=== Exercise 6: Complex Algorithm Implementation with Classes ===")
    winning_ticket = lottery_ticket(list(range(1, 16)), 4)
    print(f"The winning ticket is {winning_ticket}.")
    count = 0
    while True:
        ticket = lottery_ticket(list(range(1, 16)), 4)
        if check_ticket(winning_ticket, ticket, 4):
            print("You won the lottery!")
            break
        else:
            print("You did not win the lottery.")
            print(f"The ticket is {ticket}.")
            count +=1
    print(f"You won the lottery after {count} tries.")

def main():
    """Main function to run all exercises"""
    parser = argparse.ArgumentParser(description='Day 7 DSP Practice')
    parser.add_argument('--exercise', type=int, choices=[1, 2, 3, 4, 5, 6], 
                       help='Run specific exercise (1-6)')
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
