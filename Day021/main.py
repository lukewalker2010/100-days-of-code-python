# Class Inheritance

# class Animal:
#     def __init__(self) -> None:
#         self.num_eyes = 2

#     def breath(self):
#         print("Inhale, exhale.")

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

#     def breath(self):
#         super().breath()
#         print("doing this underwater.")

#     def swim(self):
#         print("moving in water")


# nemo = Fish()
# nemo.swim()
# nemo.breath()
# print(nemo.num_eyes)

# Slicing

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "me", "fa", "so", "la", "ti")

print(piano_keys[2:5])
print(piano_keys[2:])
print(piano_keys[:5])
print(piano_keys[2:5:2])
print(piano_keys[::2])
print(piano_keys[::-1])

print(piano_tuple[2:5])