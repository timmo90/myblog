# -*- coding: utf-8 -*-
# created by timmo on 2017/12/7

from flask_admin import BaseView, expose 
from flask_admin.contrib.sqla import ModelView
from models import *
import time
from flask import request, render_template, url_for, redirect
from myblog import db

class ArticleView(ModelView):
	can_create = False
	can_edit = True
	can_delete = True
	can_export = True
	export_types = ['csv', 'xlsx']
	page_size = 30

	column_list = ['id', 'title', 'summary', 'pub_time']
	column_labels = {'title': 'Title', 'summary': 'Summary', 'pub_time': 'Pab_time'}

	def _date_formatter(view, context, model, name):
		return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(model.pub_time))
	
	column_formatters = {'pab_time': _date_formatter}

class CreateArticle(BaseView):
	@expose('/', methods=['GET', 'POST'])
	def index(self):
		return render_template('create_article.html', create_url = url_for('createarticle.create_article'))

	@expose('/create_article', methods=['GET', 'POST'])
	def create_article(self):
		title = request.form.get('title', type = str, default = None)
		summary = request.form.get('summary', type = str, default = None)
		content = request.form.get('content', type = str, default = None)
		tags = request.form.get('tags', type = str, default = None)
		if tags:
			tags = tags.split(' ')
		else:
			tags = []
		if title and summary and content:
			article = Article(title, summary, content, tags)
			db.session.add(article)
			db.session.commit()
			return 'add article successfully'
		return redirect(url_for('createarticle.index'))


		