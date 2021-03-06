# -*-coding: utf-8 -*-
# created by timmo on 2017/10/29

from flask import Flask, render_template, url_for, redirect, flash, request
from flask_bootstrap import Bootstrap 
import config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, distinct
from form import PublishForm
from flask_admin import Admin, AdminIndexView
from flask_basicauth import BasicAuth 

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
basic_auth = BasicAuth(app)
admin = Admin(app, name=u'admin', index_view=AdminIndexView(name=u'Index', template='admin_index.html'))

from models import Article, Tag, create_article, articles_tags
import utils

@app.route('/')
def index():
	page = request.args.get('page', 1, type = int)
	pagination = Article.query.order_by(Article.pub_time.desc()).paginate(page, 
		per_page = config.MYBLOG_ARTICLE_PER_PAGE, error_out = False)
	return render_template('index.html', pagination = pagination)

@app.route('/article/<id>')
def article(id):
	article = Article.query.get_or_404(id)
	return render_template('page.html', article = article)

@app.route('/about')
def about():
	return render_template('about_me.html')

@app.route('/tags')
def tags():
	page = request.args.get('page', 1, type = int)
	pagination = Tag.query.order_by(Tag.id.desc()).paginate(page, per_page = 
		config.MYBLOG_ARTICLE_PER_PAGE, error_out = False)
	return render_template('tags.html', pagination = pagination)

@app.route('/tag/<id>')
def tag(id):
	tag = Tag.query.get_or_404(id)
	# articles = tag.articles.all()
	page = request.args.get('page', 1, type = int)
	pagination = tag.articles.order_by(Article.pub_time.desc()).paginate(page,
		per_page = config.MYBLOG_ARTICLE_PER_PAGE, error_out = False)
	# articles = pagination.items
	return render_template('tag.html', tag = tag, pagination = pagination)

@app.route('/publish', methods = ['GET', 'POST'])
def publish():
	form = PublishForm()
	if form.validate_on_submit():
		title = form.title.data
		summary = form.summary.data
		content = form.content.data
		tags = form.tags.data.split(' ')
		publish_code = form.publish_code.data
		if publish_code == config.CODE:
			article = Article(title, summary, content, tags)
			return redirect(url_for('index'))
		else:
			flash('publish_code is wrong, please try again!')
			form.publish_code.data = ''
	return render_template('publish.html', form = form)

@app.errorhandler(404)
def page_not_found(error):
	title = unicode(error)
	message = error.description
	return render_template('error.html', title = title, message = message)

@app.errorhandler(500)
def internal_server_error(error):
	title = unicode(error)
	message = error.description
	return render_template('error.html', title = title, message = message)

@app.errorhandler(502)
def bad_gateway(error):
	title = unicode(error)
	message = error.description
	return render_template('error.html', title = title, message = message)
	
from views import *

admin.add_view(ArticleView(Article, db.session, name=u'Article'))
admin.add_view(CreateArticle(name='Create'))