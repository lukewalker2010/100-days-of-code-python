# Dictionaries Deep Dive
# Key = Word in Dictionary
# Value = Definition of word

# {key: value}

# Ensure the datatype is right when defining and calling the dictionary (providing the key)

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that can be called over and over again.",
#     "Loop": "The action of doing something over and over again.",
#     }

# print(programming_dictionary["Bug"])

# programming_dictionary["Loop Again"] = "The action of doing something over and over again."

# print(programming_dictionary)

# # Create an empty dictionary
# empty_dictionary = {}

# # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in an dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# # Nesting lists and dictionaries
#     # {key: [value],
#     #  key: {value}}

# # Nesting
#     capitals = {
#         "France": "Paris",
#         "Germany": "Berlin",
#     }

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamber", "Stuttgart"],
# }

# # dictionary in dictionary

# travel_log = {
#     "France": {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamber", "Stuttgart"], "total_visits": 5},
# }

# # Nesting dictionary in list

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited" : ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#         },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamber", "Stuttgart"],
#         "total_visits": 5
#         },
# ]

import os

# Secret Auction Program
print("LOGO")
print("Welcome to the secret auction program\n")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    # {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')


