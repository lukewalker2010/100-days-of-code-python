# Turtle Graphics, Tuples, and Importing Modules
# when using more than 3 times use from turtle import Turtle otherwise just use turtle.Turtle()
# import turtle as t

from turtle import Turtle, Screen
import random
# from turtle import *
# from random import * unusal to import everything with star as you won't know where it came from
# import turtle as t
# tod = t.Turtle()

# choice([1, 2, 3])

tim = Turtle()
# tom = Turtle()
# terry = Turtle()
tim.shape("turtle")
tim.color("OrangeRed1")

# Draw a box
# for _ in range(4):
#     tim.forward(200)
#     tim.right(90)

# import heroes 
# print(heroes.gen())

# Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(["Blue", "Green", "Red", "Orange", "Yellow", "Purple"]))
    draw_shape(shape_side_n)


















screen = Screen()
screen.exitonclick()