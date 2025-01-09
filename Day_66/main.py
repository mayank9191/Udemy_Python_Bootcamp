from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random as r

app = Flask(__name__)

# CREATE DB


class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


def to_dict(self):

    if isinstance(self, list):  # It returns the bool value
        all_cafes = []
        for i in self:
            all_cafes.append({column.name: getattr(i, column.name)
                              for column in i.__table__.columns})

        if len(all_cafes) == 0:
            all_cafes.append(
                {"error": {"Not Found": "Sorry, we don't have a cafe at that location."}})

        return all_cafes

    else:
        return {column.name: getattr(self, column.name)
                for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
# In order to do return json we have to turn our random_cafe SQLAlchemy Object into a JSON. This process is called '''serialization'''

@app.route("/random", methods=["GET"])
def random():
    with app.app_context():

        random_cafe = r.choice(db.session.execute(
            db.select(Cafe)).scalars().all())
        result = to_dict(random_cafe)

    return jsonify(cafe=result)


@app.route("/all", methods=["GET"])
def all():
    with app.app_context():
        all = db.session.execute(db.select(Cafe)).scalars().all()

    return jsonify(cafe=to_dict(all))


@app.route("/search")
def search():
    l = request.args.get("loc")

    loc = db.session.execute(db.select(Cafe).where(
        Cafe.location == l.title())).scalars().all()

    return jsonify(cafe=to_dict(loc))
# HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add():

    with app.app_context():
        new_cafe = Cafe(
            name=request.form.get("name").title(),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location").title(),
            has_sockets=bool(request.form.get("has_sockets")),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"))

        db.session.add(new_cafe)
        db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    with app.app_context():
        change = db.session.execute(
            db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if change == None:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404

        change.coffee_price = new_price
        db.session.commit()

        return jsonify(success="Successfully updated the price.")


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_aCafe(cafe_id):
    api_key = request.args.get("api-key")

    if api_key == "TopSecretAPIKey":
        with app.app_context():
            to_delete = db.session.execute(
                db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
            if to_delete != None:
                db.session.delete(to_delete)
                db.session.commit()
                return jsonify(success="Successfully Deleted!"), 200

            else:
                return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key."), 403


if __name__ == '__main__':
    app.run(debug=True)
