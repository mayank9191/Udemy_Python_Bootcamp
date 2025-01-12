from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, and_
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        hashed_and_salted_password = generate_password_hash(
            password=request.form.get("password"), method="pbkdf2", salt_length=8)
        check = db.session.execute(db.select(User).where(
            User.email == email)).scalar()
        if check != None:
            flash(message="You've already signed up with that email, Login instead!")
            return redirect("/login")

        add_user = User(
            email=email, password=hashed_and_salted_password, name=name)
        db.session.add(add_user)
        db.session.commit()

        login_user(add_user)

        return redirect(f"/secrets/{name}")

    return render_template("register.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.session.execute(
            db.select(User).where(User.email == email)).scalar()

        if user == None:
            flash("That email does not exist, please try again.")
            return redirect("/login")

        if check_password_hash(pwhash=user.password, password=password):
            login_user(user)
            return redirect(f"/secrets/{user.name}")

        else:
            flash("Password incorrect, please try again.")
            return redirect("/login")

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", user=name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/download')
@login_required
def download():
    # as_attachment=True it make user to download a file send otherwise open in browser only
    return send_from_directory(directory="static", path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
