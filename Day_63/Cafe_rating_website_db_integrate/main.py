import csv
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, URL, Length
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float, Text


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes-ratings.db"
db = SQLAlchemy(model_class=Base)

db.init_app(app)


class Cafe_rating(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    cafe_name: Mapped[str] = mapped_column(
        String(250), nullable=False)
    location: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    open_time: Mapped[str] = mapped_column(String(250), nullable=False)
    close_time: Mapped[str] = mapped_column(String(250), nullable=False)
    coffee: Mapped[str] = mapped_column(Text, nullable=False)
    wifi: Mapped[str] = mapped_column(Text, nullable=False)
    power: Mapped[str] = mapped_column(Text, nullable=False)


with app.app_context():
    db.create_all()


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe Name', validators=[DataRequired()])
    cafe_location = URLField(label="Cafe Location on Google Map (URL)", validators=[Length(
        max=200), DataRequired(), URL(require_tld=True)])
    open_time = StringField(label="Opening Time e.g. 8AM",
                            validators=[DataRequired()])
    close_time = StringField(
        label="Closing Time e.g. 5:30PM", validators=[DataRequired()])

    coffee_rating = SelectField(label="Cofee Rating", choices=[(
        "☕", "☕"), ("☕☕", "☕☕"), ("☕☕☕", "☕☕☕"), ("☕☕☕☕", "☕☕☕☕"), ("☕☕☕☕☕", "☕☕☕☕☕")], validators=[DataRequired()])

    wifi_rating = SelectField(
        label="Wifi Strength Rating", choices=[("✘", "✘"), ("💪", "💪"), ("💪💪", "💪💪"), ("💪💪💪", "💪💪💪")], validators=[DataRequired()])
    socket_rating = SelectField(label="Power Socket Availability", choices=[(
        "✘", "✘"), ("🔌", "🔌"), ("🔌🔌", "🔌🔌"), ("🔌🔌🔌", "🔌🔌🔌")], validators=[DataRequired()])

    submit = SubmitField(label='Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data.title()
        cafe_location = form.cafe_location.data
        openT = form.open_time.data.upper()
        closeT = form.close_time.data.upper()
        coffeeR = form.coffee_rating.data
        wifiR = form.wifi_rating.data
        socket = form.socket_rating.data

        with app.app_context():
            cafe_add = Cafe_rating(cafe_name=cafe, location=cafe_location, open_time=openT,
                                   close_time=closeT, coffee=coffeeR, wifi=wifiR, power=socket)

            db.session.add(cafe_add)
            db.session.commit()
            print("New cafe added successfully!")
            return redirect("/add")

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with app.app_context():
        read_ratings = db.session.execute(
            db.select(Cafe_rating)).scalars().all()

        # print(read_ratings[0].cafe_name)

        return render_template('cafes.html', cafes=read_ratings)


@app.route("/delete?id=<id>")
def delete(id):
    with app.app_context():
        to_delete = db.session.execute(
            db.select(Cafe_rating).where(Cafe_rating.id == id)).scalar()
        db.session.delete(to_delete)
        db.session.commit()

        return redirect("/cafes")


if __name__ == '__main__':
    app.run(debug=True)
