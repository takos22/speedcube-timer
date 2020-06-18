from flask import Flask, render_template, redirect, url_for, request, session, send_from_directory
from flaskext.mysql import MySQL
import markupsafe as ms
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'for dev')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'chat'

mysql = MySQL(app)


@app.route("/")
def index():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", username=ms.escape(session["username"]))


@app.route("/timer")
def timer():
    if "username" not in session:
        return redirect(url_for("login"))
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * from User")
    data = cursor.fetchone()
    print(data)

    return render_template("index.html", username=ms.escape(session["username"]))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("logout.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "favicon.ico", mimetype="image/icon")
