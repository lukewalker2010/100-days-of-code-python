#Conditional flows with if / else and conditional opperators


# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm? "))
# age = int(input("What is your age in years? "))

# bill = 0

# if height >= 120:
#     print("You can ride this ride!")
#     if age < 12:
#         print("Child tickets are $5.")
#         bill = 5
#     elif age <= 18:
#         print("Youth tickets are $7.")
#         bill = 7
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be okay. Have a free ride on us!")
#     else:
#         print("Adult tickets are $12.")
#         bill = 12

#     wants_photo = input("Do you want a photo taken? Y or N. ")

#     if wants_photo == "Y":
#         #Add $3 to their bill
#         bill += 3
#     print(f"Your bill is ${bill:0.2f}")


# else:
#     print("Sorry, you can't ride this one yet.")

# Leap Year Calculator
# year = int(input())

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")


# Logical Opperators
# and 
# or
# not

print("Welcome to treasure island. Your mission is to find treasure")
choice1 = input('You\'re at a crossroad, where would you like to go? Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")





#== checks to see if it is the same vs = asigns something. == is a condition. != is not equals to.
# % moduolo checks to see if there is a remainder
    
# can use three single quotes for a multiple line print statement
