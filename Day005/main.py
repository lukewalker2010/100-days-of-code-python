# Day 5 For Loops, Range, 

# Loop allows you to execute the same code multiple times
# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# a = 0
# b = 101
# sum = 0

# for number in range(a, b):
#     print(number)
#     sum += number

# print(sum)

# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for sym in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for num in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for sym in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char
print(f"Your password is: {password}")