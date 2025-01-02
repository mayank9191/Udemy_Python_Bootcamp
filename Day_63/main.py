from flask import Flask, render_template, request, redirect, url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", library=all_books)


@app.route("/add")
def add():

    return render_template("add.html")


@app.route("/add", methods=["POST", "GET"])
def receive_data():
    book_name = request.form["book_name"]
    book_author = request.form["book_author"]
    rating = request.form["rating"]

    all_books.append(
        {"title": book_name, "author": book_author, "rating": rating})
    print(all_books)
    return redirect("/add")


if __name__ == "__main__":
    app.run(debug=True)
