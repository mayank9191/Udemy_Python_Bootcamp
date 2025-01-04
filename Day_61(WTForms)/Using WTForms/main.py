from flask import Flask, render_template, redirect
# used to create forms with help of WTForms of Flask
from flask_wtf import FlaskForm
# type of Input (text,password,submit)
from wtforms import StringField, PasswordField, SubmitField
# majorly we uses WTForms of Flask becoz of validators to check for inputed field whether wrong or right (email is with "@") besides writing individual logics
from wtforms.validators import DataRequired, Email, Length

# Making a class that inherits FlaskForm class


class MyForm(FlaskForm):
    # Different fields in a form
    email = StringField(label="Email", validators=[
                        Length(min=4, message=('Little short for an email address?')), DataRequired(), Email(message="That\'s not a valid email address.")])
    password = PasswordField(label="Password", validators=[Length(
        min=8, message=("Password must be at least 8 characters long.")), DataRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)

app.secret_key = "hello123"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()   # Object created from MyForm classs
    if form.validate_on_submit():
        # Checking for validation on submit
        email = form.email.data
        password = form.password.data
        if (email == "mayankkulahara@gmail.com" and password == "Kulahara@1234"):
            return render_template("success.html")
        else:
            return render_template("denied.html")

            # Rendering again login form
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
