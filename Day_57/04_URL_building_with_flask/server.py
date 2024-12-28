from flask import Flask, render_template
import requests
import random
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year

    return render_template("index1.html", num=random_number, year=current_year)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    all_posts = requests.get(
        url="https://api.npoint.io/c790b4d5cab58020d391").json()

    return render_template("index.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
