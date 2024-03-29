# Day 8
# Functions and Caesar Cipher

# def my_function(something):
#     # Do this with something
#     # Then do this
#     # Then do this


# def greet(name):
#     print(f"Hello, {name}")
#     print(f"How do you do {name}?")
#     print(f"Isn't the weather nice today, {name}?")

# greet("Jack Bauer")

# Functions with more than 1 input

# def greet_with(name, location):
#     print(f"Hello, {name}")
#     print(f"What is it like in {location}?")

# # greet_with(name = "Jack Bauer", location = "Nowhere")
# greet_with("Jack Bauer", "Nowhere")

# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The encoded text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text,shift_amount=shift)

# Simplify
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrpyte, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    result = input("Type 'yes' if you want to go again. otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")