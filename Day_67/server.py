from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()
emailID = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)
# Use local files instead of the default CDN
app.config['CKEDITOR_SERVE_LOCAL'] = True
# Ensure the package type matches your CKEditor version
app.config['CKEDITOR_PKG_TYPE'] = 'full'


# Form structure to add new post and edit a form


class PostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    name = StringField(label="Your Name", validators=[DataRequired()])
    img = StringField(label="Blog Image URL", validators=[DataRequired()])
    body = CKEditorField(label="Blog Content")
    submit = SubmitField(label="SUBMIT POST")


# Creating Database
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), nullable=False, unique=True)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[Text] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# Landing Page with all the log posts
@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

# Go to specific post to see whole post


@app.route("/show_post?id=<int:post_id>")
def show_post(post_id):

    requested_post = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)

# To craete a new post in Blogster


@app.route("/new_post", methods=["GET", "POST"])
def add_new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        name = form.name.data
        img_url = form.img.data
        body = form.body.data

        new_post = BlogPost(title=title, date=date.today().strftime("%B %d, %Y"),
                            body=body, author=name, img_url=img_url, subtitle=subtitle)
        db.session.add(new_post)
        db.session.commit()

        return redirect("/")
    return render_template("make-post.html", form=form, change=False)

# To edit a post choosen


@app.route("/edit?post_id=<int:id>", methods=["GET", "POST"])
def edit_post(id):

    post = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == id)).scalar()
    # populate allready filled data from database
    form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        name=post.author,
        img=post.img_url,
        author=post.author,
        body=post.body
    )
    # is_string = isinstance()
    if form.validate_on_submit():
        post_edit.title = form.title.data
        post_edit.date = date.today().strftime("%B %d, %Y")
        post_edit.body = form.body.data
        post_edit.author = form.name.data
        post_edit.img_url = form.img.data
        post_edit.subtitle = form.subtitle.data
        db.session.commit()

        return redirect(f"/show_post%3Fid={id}")
    return render_template("make-post.html", form=form, change=True)

# To delete a post from database


@app.route("/delete?post_id=<int:id>")
def delete_post(id):
    to_delete = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == id)).scalar()
    db.session.delete(to_delete)
    db.session.commit()

    return redirect("/")

# About page


@app.route("/about")
def about():
    return render_template("about.html")

# Contact form


@app.route("/contact", methods=["POST", "GET"])
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
    app.run(debug=True)
