# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class to_do_Form(FlaskForm):
	body = TextAreaField('待办事项:', validators=[DataRequired(), Length(1,200)])
	submit = SubmitField('新增')