# Higher or lower game

# Compare  who has higher or lower followers on instagram
# Keep track of the score

from art import logo, vs
from game_data import data
import random
import os
 
# Format the account data into a printable format
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
       return guess == "a"
    else:
       return guess == "b"
   
# Display Art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:

    # Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)
        
    print(f"Comapare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    # Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls')
    print(logo)

    # Use if statement to check if user is correct.
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score {score}.")


# Clear the screen between rounds
