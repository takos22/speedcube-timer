import os
import markupsafe as ms
from flask import flash, redirect, render_template, request, send_from_directory, session, url_for
from timer import app
from timer.forms import LoginForm


@app.route("/")
def index():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("public/index.html", username=ms.escape(session["username"]))


@app.route("/timer")
def timer():
    if "username" not in session:
        return redirect(url_for("login"))

    times = [30, 42, 37, 36, 48, 25]
    return render_template("public/timer.html", username=ms.escape(session["username"]), times=times[:10 if len(times) >= 10 else None], enumerate=enumerate)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}")
        return redirect(url_for("index"))
    return render_template("public/login.html", form=form)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("public/logout.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "favicon.ico", mimetype="image/icon")
