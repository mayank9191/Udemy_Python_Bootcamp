from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, LoginForm, RegisterForm
from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()

emailID = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)
# Use local files instead of the default CDN
app.config['CKEDITOR_SERVE_LOCAL'] = True
# Ensure the package type matches your CKEditor version
app.config['CKEDITOR_PKG_TYPE'] = 'full'


# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# TODO: Create a User table for all your registered users.
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_name: Mapped[str] = mapped_column(
        String(250), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(
        String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    # comment:Mapped[Text] = mapped_column(Text,nullable=False)


with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["POST", "GET"])
def register():
    registerform = RegisterForm()
    if registerform.validate_on_submit():
        hashed_pass = generate_password_hash(
            password=registerform.password.data, method="pbkdf2", salt_length=8)
        new_user = User(user_name=registerform.name.data,
                        email=registerform.email.data, password=hashed_pass)
        # login_user(new_user)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("get_all_posts"))

    return render_template("register.html", form=registerform)


# TODO: Retrieve a user from the database based on their email.
@app.route('/login')
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        return redirect(url_for("get_all_posts"))

    return render_template("login.html", form=loginform)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        img_url = form.img_url.data
        body = form.body.data

        new_post = BlogPost(title=title, subtitle=subtitle, date=date.today().strftime("%B %d, %Y"),
                            body=body, img_url=img_url)

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=emailID, password=password)
            connection.sendmail(from_addr=emailID, to_addrs=emailID, msg=f'''Subject:New Message\n\nName:{
                                name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}''')
            return redirect("/")
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
