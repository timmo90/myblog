# -*-coding: utf-8 -*-
# created by timmo on 2017/10/29

from flask import Flask, render_template, url_for, redirect
import config
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

from models import Article, Tag, create_article
import utils

@app.route('/')
def index():
	pagination = Article.query.order_by(Article.id.desc()).paginate(1, 
		per_page = config.MYBLOG_ARTICLE_PER_PAGE, error_out = False)
	return render_template('index.html', pagination = pagination)

@app.route('/article/<id>')
def article(id):
	article = Article.query.get_or_404(id)
	return render_template('page.html', article = article)
