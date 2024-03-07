# Google Pixel Superfans 
# Pixel Pulse / Vol 5
# Image says CAMERA OBSCURA

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


cipher = "27 _ _ 4 _ 14 _ 16 _ 8 _ 20 11 _ _ 16 _ _ _ _ _ _ 14 20 6 _ _ _ _ _ 14 14 9 14 7 _ 23 _ 25"
split_ciper = cipher.split(" ")

word = ""

for i in split_ciper:
    if i == "_":
        word += "_"
        print("_")
    elif i == " ":
        word += " "
        print(" ")
    else:
        word += alphabet[int(i)-1]
        print(alphabet[int(i)-1])

print(word)

