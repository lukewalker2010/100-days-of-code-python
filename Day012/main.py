# Day012

# Scope

# enemies = 1

# def increase_enemies():
#     enemies = 2 
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope
# def drink_potion():
#     postion_strength = 2
#     print(postion_strength)

# drink_potion()
# # print(postion_stength)

# # Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         postion_strength = 2
#         print(player_health)

#     drink_potion()

# print(player_health)

# There is no Block Scope

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

# Global Variable
# enemies = 1

# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global constatnst
# PI = 3.14159
# URL = "http://www.google.com"

# Number Guessing Game!
import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users guess against answer
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"you got i! the answer was {answer}.")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1,100)

    # Function to let the user guess a number
    turns = set_difficulty()


    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses you loose.")
            return
        elif guess != answer:
            print("Guess again")

# Track the number of turns and reduce by 1 if they get it wrong

game()