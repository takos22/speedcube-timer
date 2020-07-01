from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from timer import views
from timer import admin_views
