#!/usr/bin/env python3
"""
Day 6 Practice - Day 6 Practice
Date: 2025-08-28
Goals: Complete Day 6 exercises
"""


import argparse

def favorite_book(title):
    """Prints a message about a favorite book"""
    print(f"One of my favorite books is {title}")

def exercise_1():
    """Exercise 1: Simple Function Definition"""
    print("=== Exercise 1: Simple Function Definition ===")
    favorite_book("The Great Gatsby")

def make_shirt(size, message):
    """Prints a message about a shirt"""
    print(f"I have a {size} shirt and it says '{message}'")

def exercise_2():
    """Exercise 2: Function Parameters and Keyword Arguments"""
    print("=== Exercise 2: Function Parameters and Keyword Arguments ===")
    make_shirt("large", "I love Python")
    make_shirt(message="I love Python", size="large")

def make_shirt_default(message="I love Python", size="large"):
    """Prints a message about a shirt"""
    print(f"I have a {size} shirt and it says '{message}'")

def exercise_3():
    """Exercise 3: Default Parameter Values"""
    print("=== Exercise 3: Default Parameter Values ===")
    make_shirt_default()
    make_shirt_default(size="medium")
    make_shirt_default(message="I love Python a lot", size="small")

def describe_city(city, country="USA"):
    """Prints a message about a city"""
    print(f"{city} is in {country}")

def exercise_4():
    """Exercise 4: Default Parameters with Override"""
    print("=== Exercise 4: Default Parameters with Override ===")
    describe_city("New York")
    describe_city("Paris", "France")
    describe_city("Tokyo", "Japan")

def city_country(city, country):
    """Prints a message about a city and country"""
    return f"{city}, {country}"

def exercise_5():
    """Exercise 5: Function Return Values"""
    print("=== Exercise 5: Function Return Values ===")
    print(city_country("New York", "USA"))
    print(city_country("Paris", "France"))
    print(city_country("Tokyo", "Japan"))

def make_album(artist, title, tracks=None):
    """Prints a message about an album"""
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album

def exercise_6():
    """Exercise 6: Optional Parameters and Conditional Logic"""
    print("=== Exercise 6: Optional Parameters and Conditional Logic ===")
    print(make_album("Artist 1", "Album 1"))
    print(make_album("Artist 2", "Album 2", 10))

def exercise_7():
    """Exercise 7: Interactive Function with User Input"""
    print("=== Exercise 7: Interactive Function with User Input ===")
    print("Simulating user input for album creation:")
    print("Artist: 'The Beatles', Title: 'Abbey Road', Tracks: '17'")
    artist = "The Beatles"
    title = "Abbey Road"
    tracks = "17"
    print(make_album(artist, title, tracks))
    
def show_messages(messages):
    """Prints a message about a list of messages"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Prints a message about a list of messages"""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def exercise_8():
    """Exercise 8: List Manipulation in Functions"""
    print("=== Exercise 8: List Manipulation in Functions ===")
    messages = ["Hello", "How are you?", "I'm fine, thank you!"]
    show_messages(messages)
    sent_messages = []
    send_messages(messages, sent_messages)
    print("\nFinal lists:")
    print("Messages:", messages)
    print("Sent messages:", sent_messages)

def exercise_9():
    """Exercise 9: List Slicing to Preserve Original"""
    print("=== Exercise 9: List Slicing to Preserve Original ===")
    messages = ["Hello", "How are you?", "I'm fine, thank you!"]
    show_messages(messages)
    sent_messages = []
    send_messages(messages[:], sent_messages)
    print("\nFinal lists:")
    print("Messages:", messages)
    print("Sent messages:", sent_messages)

def sandwich_order(items):
    """Prints a message about a sandwich order"""
    print("I'll make you a great sandwich:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!")

def exercise_10():
    """Exercise 10: Variable-Length Arguments (*args)"""
    print("=== Exercise 10: Variable-Length Arguments (*args) ===")
    sandwich_order(["lettuce", "tomato", "onion"])
    sandwich_order(["lettuce", "tomato", "onion", "ham"])
    sandwich_order(["lettuce", "tomato", "onion", "ham", "cheese"])

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

def exercise_11():
    """Exercise 11: Keyword Arguments (**kwargs)"""
    print("=== Exercise 11: Keyword Arguments (**kwargs) ===")
    user_profile = build_profile('John', 'Doe', location='New York', field='Engineering')
    print(user_profile)

def make_car(manufacturer, model, **car_info):
    """Make a dictionary representing a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

def exercise_12():
    """Exercise 12: Advanced Keyword Arguments with Dictionary Building"""
    print("=== Exercise 12: Advanced Keyword Arguments with Dictionary Building ===")
    car = make_car('subaru', 'outback', color='blue', tow_package=True)
    print(car)

def main():
    """Main function to run all exercises"""
    parser = argparse.ArgumentParser(description='Day 6 DSP Practice')
    parser.add_argument('--exercise', type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
                       help='Run specific exercise (1-12)')
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


if __name__ == "__main__":
    main()
