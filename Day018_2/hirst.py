# import colorgram

# rgb_colors = []
# colors = colorgram.extract('C:/Users/luwalker/Documents/python/100-days-of-code-python/100-days-of-code-python/Day018_2/image.jpg', 20)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(209, 165, 125), (249, 234, 237), (140, 48, 106), (164, 169, 38), (244, 80, 56), (3, 143, 55), (233, 109, 162), (215, 234, 232), (241, 65, 140), (1, 143, 184), (162, 55, 52), (57, 202, 224), (254, 230, 0), (20, 166, 126), (211, 232, 236), (244, 223, 50), (27, 197, 219), (162, 184, 171), (233, 165, 191)]

import turtle as t
import random

tim = t.Turtle()
tim.speed('fastest')
t.colormode(255)
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range (1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = t.Screen()
screen.exitonclick()