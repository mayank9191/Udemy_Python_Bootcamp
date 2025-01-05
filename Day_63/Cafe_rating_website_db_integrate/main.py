import csv
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, URL, Length
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes-ratings.db"
db = SQLAlchemy(model_class=Base)

d


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
        cafe = form.cafe.data
        cafe_location = form.cafe_location.data
        openT = form.open_time.data
        closeT = form.close_time.data
        cofeeR = form.coffee_rating.data
        wifiR = form.wifi_rating.data
        Socket = form.socket_rating.data
        with open("cafe-data.csv", "a", encoding="utf-8") as f:
            f.write(f'''{cafe},{cafe_location},{openT},{
                closeT},{cofeeR},{wifiR},{Socket}\n''')
        print("New cafe added successfully!")
        return redirect("/add")

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open("cafe-data.csv", newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
