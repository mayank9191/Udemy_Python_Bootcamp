from flask import Flask, render_template, request, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
'''
We Want to show that why database is needed as we can save a data into a data structure like list as it is volatile in nature  we will learn basics of SQLite Database
'''

app = Flask(__name__)

# Create Database


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)

# Create Table feilds (Schema)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Creation
with app.app_context():
    db.create_all()


@app.route('/')
def home():

    # data read from database
    with app.app_context():
        result = db.session.execute(db.select(Book))
        all_books = result.scalars().all()

    return render_template("index.html", library=all_books)


@app.route("/add")
def add():

    return render_template("add.html")

# Different Route to get filled data in form by methods=["POST"]


@app.route("/add", methods=["POST", "GET"])
def receive_data():
    book_name = request.form["book_name"]
    book_author = request.form["book_author"]
    rating = request.form["rating"]

    # data added  into form is added into the database

    with app.app_context():
        new_book = Book(title=book_name, author=book_author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

    return redirect("/")


@app.route("/edit?id=<id>")
def edit(id):
    with app.app_context():
        book_details = db.session.execute(
            db.select(Book).where(Book.id == id)).scalar()

    title = book_details.title
    rating = book_details.rating

    return render_template("edit.html", id=id, title=title, rating=rating)


@app.route("/edit/<id>", methods=["POST", "GET"])
def update_db(id):
    # Update Database
    print(request.form["new_rating"])
    with app.app_context():
        book_to_edit = db.session.execute(
            db.select(Book).where(Book.id == id)).scalar()

        book_to_edit.rating = request.form["new_rating"]
        db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
