# Hangman

# Steps
# Generate a random word
# Generate as many blanks as there are letters in the word
# Ask the user to guess a letter
# Check if the letter is in the word
# See if they have filled all the blanks
# If not letter, lose a life, and check and see if they run out of lives
# Game over

import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#DEBUG
print(f"Psst, the solution is {chosen_word}.")

num_lives = 10

while num_lives < 10:
    guess = input("Guess a letter: ").lower()

    display = []
    for _ in range(word_length):
        display += "_"

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    num_lives += 1