# -*- coding: utf-8 -*-

from flask import flash, redirect, url_for, render_template

from app import app, db
from forms import to_do_Form
from models import Thing

@app.route('/', methods = ['GET', 'POST'])
def index():
	things = Thing.query.filter_by(status=True).order_by(Thing.timestamp.desc()).all()
	form = to_do_Form()
	if form.validate_on_submit():
		body = form.body.data
		thing = Thing(body=body)
		db.session.add(thing)
		db.session.commit()
		flash('待办事项已经添加！')
		return redirect(url_for('index'))
	return render_template('index.html', form=form, things=things)

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
	thing = Thing.query.filter_by(id=id).first()
	thing.status = False
	db.session.commit()
	return redirect(url_for('index'))


