from flask import Flask

# Basic Flask App
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return "Bye!"


if __name__ == "__main__":
    app.run()
