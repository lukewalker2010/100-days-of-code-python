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
end_of_game = False
lives = 6
stages = ["1", "2", "3", "4", "5", "6", "7"]
logo = "Hangman"

print(logo)

#DEBUG
print(f"Psst, the solution is {chosen_word}.")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])