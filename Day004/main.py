# Day 4

# randomization and lists
# Mersenne Twister is what python uses
# Khan acadamy has a good video on psudo random numbers

# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# # 0.00000 - 9.999999...
# random_float = random.random()
# print(random_float)

# # 0.0000000 - 4.99999999
# random_float *= 5
# print(random_float)

# love_score = random.randint(1,100)
# print(f"your love score is {love_score}")


# Importing other modules
# import my_module
# print(my_module.pi)

# Lists (ways of storing data)

# fruits = ["Cherry", "Apple", "Pear"]

# states_of_America = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "connecticut",
#                      "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York"]
# states_of_America[1] = "Pencilvania"
# states_of_America.append("Walker Homestead") # Adds one item
# states_of_America.extend(["Walker", "Lukley"]) # Adds a list to a list

# num_of_states = len(states_of_America)

# print(states_of_America[num_of_states-1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Potatoes"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][1])


# Rock paper scissors game

import random

rock = "Rock"
paper = "Paper"
Scissors = "Scissors"

user_choise = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

computer_choise = random.randint(0,2)
print(f"Comuter chose {computer_choise}")

if user_choise == computer_choise:
    print("It is a draw")
elif user_choise == 0 & computer_choise == 2:
    print("You win")
