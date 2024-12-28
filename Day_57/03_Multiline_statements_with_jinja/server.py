from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/blog")
def blog():
    all_posts = requests.get(
        url="https://api.npoint.io/c790b4d5cab58020d391").json()

    return render_template("index.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
