# Draw a random walk
# Tuple = (1, 3, 8)
# Tuple can't change values like you can a list

import turtle as t
import random


# # Random Walk
# tim = t.Turtle()

# direction = [0, 90, 180, 270]
# # colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

# def random_color():
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     random_color = (r, g, b)
#     return random_color

# tim.pensize(10)
# tim.speed(10)

# t.colormode(255)
# for _ in range (200):
#     tim.forward(30)
#     tim.setheading(random.choice(direction))
#     tim.color(random_color())


# screen = t.Screen()
# screen.exitonclick()


# Spirograph
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()



