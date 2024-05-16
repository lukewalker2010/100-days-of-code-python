# Errors and Exceptions

# File not found
try:
    file = open("a_file.txt")
except:
    print("There was an error")

# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Try
# Except
# Else
# Finally