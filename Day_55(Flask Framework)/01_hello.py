from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return "Goodbye!"


# To pass the name in the URL(as variable) and converting the path to a specific data type
@app.route("/username/<name>/<int:number>")
def greet_name(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
   # Run the app in debug mode to auto-reload the server when the code changes
    app.run(debug=True)
