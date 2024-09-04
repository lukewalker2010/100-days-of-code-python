from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0,9)

@app.route('/')
def hello_world():
    #Rendering HTML Elements
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'



#Creating variable paths and converting the path to a specified data type
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_num:
        return  '<h1 style="text-align: center; color: purple">Too high, try again!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>'

    elif guess < random_num:
        return  '<h1 style="text-align: center; color: red">Too low, try again!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200>' 

    else:
        return  '<h1 style="text-align: center; color: green">You found me!</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200>'


if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
