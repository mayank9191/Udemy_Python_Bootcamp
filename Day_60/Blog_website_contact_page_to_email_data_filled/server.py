from flask import Flask, render_template, request, redirect
import requests
from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()
emailID = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

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


@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/post/<int:num>")
def show_post(num):
    if num == 1:
        title = response[num-1]["title"]
        subtitle = response[num-1]["subtitle"]
        body = response[num-1]["body"]
        img = "https://inbloomflorist.flowermanager.net/wp-content/uploads/sites/23/2021/06/July-Plant-of-the-Month_Cactus-1-of-11-1200x800.jpg"

        return render_template("post.html", title=title, subtitle=subtitle, body=body, img=img)

    elif num == 2:
        title = response[num-1]["title"]
        subtitle = response[num-1]["subtitle"]
        body = response[num-1]["body"]
        img = "https://static.freemake.com/blog/wp-content/uploads/2015/05/Bored-Online-what-to-do.jpg"

        return render_template("post.html", title=title, subtitle=subtitle, body=body, img=img)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phoneNo = request.form["phoneNo"]
    message = request.form["message"]

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=emailID, password=password)
        connection.sendmail(from_addr=emailID, to_addrs=emailID,
                            msg=f'''Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phoneNo}\nMessage: {message}''')
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
