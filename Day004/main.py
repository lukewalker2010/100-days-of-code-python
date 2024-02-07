# Day 4

# randomization and lists
# Mersenne Twister is what python uses
# Khan acadamy has a good video on psudo random numbers

import random


random_integer = random.randint(1, 10)
print(random_integer)

# 0.00000 - 9.999999...
random_float = random.random()
print(random_float)

# 0.0000000 - 4.99999999
random_float *= 5
print(random_float)

love_score = random.randint(1,100)
print(f"your love score is {love_score}")

# import my_module
# print(my_module.pi)

