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
from urllib.parse import urlencode

URL = "https://api.themoviedb.org/3/search/multi"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiN2YwZjY1MWY1ZTUyMmM3MzYyMDNlNjFhMmU3N2ZiZiIsIm5iZiI6MTczNjE4NDYzMy43MTQsInN1YiI6IjY3N2MxMzM5MTU1MjFmODNkOTY3MjNjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tP-RQjsGKWti5w2O1PGh3NcMYiw-Fhu1tAYYZiV92pU "

}

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

bootstrap = Bootstrap5(app)
# WTFORMS


class Movie_add(FlaskForm):
    title = StringField(label="Movie Name", validators=[DataRequired()])
    # music = FileField(label="Add Music from that movie",
    #                   validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


class Rating_edit(FlaskForm):
    new_rating = IntegerField(label="Rank it Out of 10",
                              validators=[DataRequired()])
    new_review = StringField(label="Your Review",
                             validators=[DataRequired()])

    submit = SubmitField(label="Done")


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
    ranking: Mapped[int] = mapped_column(Integer, unique=True, nullable=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
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

        title = form.title.data
        parameter = {
            "query": title
        }

        response = requests.get(url=URL, headers=headers, params=parameter)

        data = response.json()["results"]
        # music = form.music.data
        # music_data = music.read()

        return render_template("select.html", data=data)

    return render_template("add.html", form=form)


@app.route("/edit?id=<int:id>", methods=["POST", "GET"])
def edit(id):

    form2 = Rating_edit()
    if form2.validate_on_submit():
        with app.app_context():
            select = db.session.execute(
                db.select(Movies).where(Movies.id == id)).scalar()
            select.ranking = form2.new_rating.data
            select.review = form2.new_review.data
            db.session.commit()

            return redirect("/")

    return render_template("edit.html", form2=form2)


@app.route("/delete?id=<id>")
def delete(id):
    with app.app_context():
        movie_to_delete = db.session.execute(
            db.select(Movies).where(Movies.id == id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()

        return redirect("/")


@app.route("/update")
def update():
    dict_data = request.args.to_dict()
    img_url = "https://image.tmdb.org/t/p/w500" + dict_data["poster_path"]
    title = dict_data.get("title") or dict_data.get("name")
    year = dict_data.get("first_air_date") or dict_data.get("release_date").split(
        "-")[0]
    rating = float(dict_data["vote_average"])
    description = dict_data["overview"]

    with app.app_context():
        new_entry = Movies(img_url=img_url, title=title,
                           year=year, rating=round(rating, 1), description=description)

        db.session.add(new_entry)
        db.session.commit()
        return redirect("/add")


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
