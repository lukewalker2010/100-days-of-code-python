# Day 13 Debugging

# Describe the problem
# Only gets to 19 as range 
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")

# my_function()

# # Reproduce the bug
# # randint(1,6) should be randint(0,5)
# from random import randint
# dice_img = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1,6)
# print(dice_img[dice_num])

# # Play computer
# # 1994 doesn't return anything
# year = int(input("What's your ear of birth?"))
# if year > 1980 and year < 1994:
#     print("you are millenial.")
# elif year >= 1994:
#     print("You are gen z.")

# # Fix the errors
# # add int to input to cast string to int
# # add f to print
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}")

# Print is your friend
# double equals
# pages = 0
# words_per_page = 0
# pages = int(input("Number of pages: "))
# # print(f"You entered {pages} pages")
# words_per_page = int(input("Number of words per page: "))
# # print(f"You entered {words_per_page} words per page")
# total_words = pages * words_per_page
# print(total_words)

# # Debugger
# # b_list.append(new_item) is at wrong level and needs another indent
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# print(mutate([1,2,3,4,5,8,13]))

# Final tips
# Take a break and walk away
# Ask a friend
# Run often
# Ask StackOverflow (Search first)
