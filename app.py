from flask import Flask, request, render_template, redirect, session
from models.user import User, find_user
from shared.db import db

app = Flask(__name__)

app.config["SECRET_KEY"] = "abS8gfjAh"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if username and email and password:
            if find_user(email):
                return render_template("register.html", error="Электронная почта занята.")

            new_user = User(username, email, password)

            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = find_user(email)

        if user and user.check_password(password):
            session["email"] = user.email
            return redirect("/index")
        else:
            return render_template("login.html", error="Неверная почта или пароль.")

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
