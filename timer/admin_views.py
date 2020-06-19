import os
from flask import redirect, render_template, request, session, url_for
import markupsafe as ms

from timer import app

@app.route("/admin")
def admin():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("admin/admin.html", username=ms.escape(session["username"]))