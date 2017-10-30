# -*-coding: utf-8 -*-
# created by timmo on 2017/10/29

from myblog import db
from datetime import datetime

articles_tags = db.Table(
	'articles_tags',
	db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
	db.Column('article_id',db.Integer, db.ForeignKey('articles.id')))

class Article(db.Model):
	__tablename__ = 'articles'

	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100))
	summary = db.Column(db.String(300))
	content = db.Column(db.Text)
	pub_time = db.Column(db.DateTime, default = datetime.now)
	tags = db.relationship('Tag',
		secondary = articles_tags,
		backref = db.backref('articles', lazy = 'dynamic'))


	def __init__(self, title, summary, content, pub_time = None):
		self.title = title
		self.summary = summary
		self.content = content
		if pub_time:
			self.pub_time = pub_time


class Tag(db.Model):
	__tablename__ = 'tags'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), unique = True)

	def __init__(self, name):
		self.name = name.lower()
		

