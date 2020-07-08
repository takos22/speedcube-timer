from timer import app
from timer.forms import LoginForm
from timer.models import User

from flask import flash, redirect, render_template, request, send_from_directory, session, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import os
import markupsafe as ms


@app.route("/")
@app.route("/home")
@login_required
def index():
    return render_template("public/index.html", current_user=current_user)


@app.route("/timer")
def timer():
    times = [30, 42, 37, 36, 48, 25] # random values for testing
    return render_template("public/timer.html", current_user=current_user, times=times[:10 if len(times) >= 10 else None], enumerate=enumerate)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)

    return render_template("public/login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("timer"))


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "favicon.ico", mimetype="image/icon")
