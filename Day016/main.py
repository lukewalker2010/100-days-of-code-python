# OOP (Object Oriented Programming)

# OBJECT
# Has things = Attributes
# Does things = Methods
# Can have multiple versions of the same objects generated (Class)
# Class -> Object
# Class is Pascal Case (FirstLetterCapatalized
# Car = CarBlueprint() -> Object = Class

# import another_module
# print(another_module.another_variable)


# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue2")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'

print(table)