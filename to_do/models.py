# -*- coding: utf-8 -*-

from datetime import datetime
from app import db

class Thing(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(200))
	status = db.Column(db.Boolean, default = True)
	timestamp = db.Column(db.DateTime, default = datetime.now(), index = True)
