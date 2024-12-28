import random
from flask import Flask

app = Flask(__name__)

random_number = random.randint(0, 9)
# print(random_number)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess_number>")
def result(guess_number):
    if (guess_number == random_number):
        return '<h1 style="color:green">You found me!</h1>'\
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width= 500 height=500>'

    elif (guess_number > random_number):
        return '<h1 style="color: purple">Too high,try again!</h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width= 500 height=500>'

    else:
        return '<h1 style="color:red">Too low,try again!</h1>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width= 500 height=500>'


if __name__ == "__main__":
    app.run(debug=True)
