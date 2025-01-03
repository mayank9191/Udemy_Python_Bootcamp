from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)

# Initialise the app with the extension
db.init_app(app)

# CREATE TABLE
# Class Name is the table's name

# Model represents Python Classes


class Book(db.Model):
    # Columns or fields
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# C.R.U.D. Operations
# CREATE RECORD
with app.app_context():
    new_book = Book(id=2, title="Atomic Habits",
                    author="James Clear", rating=10)
    db.session.add(new_book)
    db.session.commit()

# Read RECORD
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()

# READ A PARTICULAR RECORD BY Query
with app.app_context():
    result = db.session.execute(db.select(Book).where(
        # scalar() is used on place of scalars() here for single data entry
        Book.title == "Harry Poter")).scalar()

# UPDATE A PARTICULAR RECORD BY Query
with app.app_context():
    book_to_update = db.session.execute(
        db.select(book).where(book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# UPDATE A RECORD BY PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(
        db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

# DELETE A PARTICULAR RECORD BY PRIMARY KEY
book_id = 1
with app.app_context():
    booK_to_delete = db.session.execute(
        select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
