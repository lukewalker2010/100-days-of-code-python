# Tkinter for GUI (Graphical User Interface)

# Arguments with Defaulte Values

# def my_function(a=1, b=2, c=1) (a, b, and c are default values)


# # Unlimted Positional Arguments
# def add(*args):
#     print(args[0])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(3, 5, 6))

# # Many Keyword Arugments
# def calculate(n, **kwargs):
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)

#     # print(kwargs["add"])

#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=5)

# # Class with optional keyword arguments
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")
        
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.make)
# print(my_car.model)
# print(my_car.color)


# Tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()

# configure or update properties of components
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Got Clicked")
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
input = Entry(width=30)
# Add some text to being with
input.insert(END, string="Some text to begin with.")
input.pack()
print(input.get())


# Text
text = Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Adds some text to being with
text.insert(END, "Example of multi-line text entry.")
# Get's current value in the textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets teh current value in spinbox.
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if on button checked, otherwise 0.
    print(checked_state.get())
# Variable to hold oon to tchecked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())
# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()