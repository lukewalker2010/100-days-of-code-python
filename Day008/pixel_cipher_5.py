# Google Pixel Superfans 
# Pixel Pulse / Vol 5
# Image says CAMERA OBSCURA

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


alphabet_reverse = alphabet[::-1]

cipher = "_ 7 _ _ 4 _ 14 _ 16 _ 8 _ 20 11 _ _ 16 _ _ _ _ _ _ 14 20 6 _ _ _ _ _ 14 14 9 14 7 _ 23 _ 25"
cipher_decryped = "A G O O D S N A P S H O T K E E P S A M O M E N T F R O M R U N N I N G A W A Y"

split_ciper = cipher.split(" ")

word = ""

for i in split_ciper:
    if i == "_":
        word += "_"
    elif i == " ":
        word += " "
    else:
        word += alphabet[int(i)-1]

word_reverse = ""

for i in split_ciper:
    if i == "_":
        word_reverse += "_"
    elif i == " ":
        word_reverse += " "
    else:
        word_reverse += alphabet_reverse[int(i)-1]


print(word)
print(word[::-1])
print(word_reverse)
print(word_reverse[::-1])





# key = ['c', 'a', 'm', 'e', 'r', 'a', ' ', 'o', 'b', 's', 'c', 'u', 'r', 'a']

# cipher = "_ 7 _ _ 4 _ 14 _ 16 _ 8 _ 20 11 _ _ 16 _ _ _ _ _ _ 14 20 6 _ _ _ _ _ 14 14 9 14 7 _ 23 _ 25"

# word = ""

# for char in cipher:
#     if char == "_":
#         word += "_"
#         # print("_")
#     elif char == " ":
#         word += " "
#         # print(" ")
#     else:
#         word += key[int(char)-1]
#         # print(alphabet[int(i)-1])

# print(word)
