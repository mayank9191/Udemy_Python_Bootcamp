from flask import Flask, redirect, request, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, URLField, FloatField, FileField
from wtforms.validators import DataRequired, Length, URL
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, LargeBinary
import requests
from io import BytesIO


app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

bootstrap = Bootstrap5(app)
# WTFORMS


class Movie_add(FlaskForm):
    img_url = URLField(label="URL of Movie Picture",
                       validators=[DataRequired(), URL(require_tld=True)])
    ranking = IntegerField(label="Rank it!", validators=[DataRequired()])
    title = StringField(label="Movie Name", validators=[DataRequired()])
    year = IntegerField(label="Year of Release", validators=[DataRequired()])
    rating = FloatField(label="Rate it!", validators=[DataRequired()])
    review = StringField(label="Write it's review",
                         validators=[DataRequired()])
    description = StringField(label="Description",
                              validators=[DataRequired()])
    # music = FileField(label="Add Music from that movie",
    #                   validators=[DataRequired()])
    submit = SubmitField(label="Submit")


# DATABASE CREATION
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    img_url: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    # music: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    with app.app_context():
        read_data = db.session.execute(db.select(Movies)).scalars().all()

    return render_template("index.html", data=read_data)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = Movie_add()
    if form.validate_on_submit():
        img_url = form.img_url.data
        ranking = form.ranking.data
        title = form.title.data
        year = form.year.data
        rating = form.rating.data
        review = form.review.data
        description = form.description.data
        # music = form.music.data
        # music_data = music.read()

        with app.app_context():
            new_entry = Movies(img_url=img_url, ranking=ranking, title=title,
                               year=year, rating=rating, review=review, description=description)

            db.session.add(new_entry)
            db.session.commit()
            return redirect("/")

    return render_template("add.html", form=form)


@app.route("/update")
def update():
    return render_template("edit.html")


@app.route("/delete?id=<id>")
def delete(id):
    with app.app_context():
        movie_to_delete = db.session.execute(
            db.select(Movies).where(Movies.id == id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()

        return redirect("/")


# @app.route("/music?id=<int:id>")
# def music(id):
#     with app.app_context():
#         mu = db.session.execute(
#             db.select(Movies).where(Movies.id == id)).scalar()

#         music_data = BytesIO(mu.music)
#         print("hello")

#         return send_file(music_data, as_attachment=False, mimetype='audio/mpeg')


if __name__ == "__main__":
    app.run(debug=True)
