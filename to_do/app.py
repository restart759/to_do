# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)

import views, commands

