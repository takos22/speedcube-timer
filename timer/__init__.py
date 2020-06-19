import os
from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'for dev')

from timer import views
from timer import admin_views