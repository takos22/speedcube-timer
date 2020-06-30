import os
from flask import redirect, render_template, request, send_from_directory, session, url_for
import markupsafe as ms

from timer import app


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
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return render_template("public/login.html")


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("public/logout.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "favicon.ico", mimetype="image/icon")
