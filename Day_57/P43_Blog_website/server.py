from flask import Flask, render_template
import requests
app = Flask(__name__)

response = requests.get(
    url="https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route("/")
def home():
    title1 = response[0]["title"]
    title2 = response[1]["title"]
    subtitle1 = response[0]["subtitle"]
    subtitle2 = response[1]["subtitle"]
    return render_template("index.html", ti1=title1, sub1=subtitle1, ti2=title2, sub2=subtitle2)


@app.route("/post/<int:num>")
def show_post(num):
    if num == 1:
        title = response[num-1]["title"]
        subtitle = response[num-1]["subtitle"]
        body = response[num-1]["body"]

        return render_template("post.html", title=title, subtitle=subtitle, body=body)

    else:
        title = response[num-1]["title"]
        subtitle = response[num-1]["subtitle"]
        body = response[num-1]["body"]

        return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
