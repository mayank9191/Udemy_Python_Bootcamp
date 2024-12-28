from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/guess/<name>")
def home(name):
    gender = requests.get(
        url=f"https://api.genderize.io/?name={name}").json()["gender"]
    age = requests.get(url=f"https://api.agify.io/?name={name}").json()["age"]
    return render_template("index.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
