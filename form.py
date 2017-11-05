# -*-coding: utf-8 -*-
# created by timmo on 2017/11/5

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PublishForm(FlaskForm):
	title = StringField('Title', validators = [Required()])
	summary = TextAreaField('Summary')
	content = TextAreaField('Content', validators = [Required()])
	tags = StringField('Tags')
	publish_code = StringField('Pub_code', validators = [Required()])
	submit = SubmitField('Submit')
		