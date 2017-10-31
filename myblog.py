# -*-coding: utf-8 -*-
# created by timmo on 2017/10/29

from flask import Flask, render_template
import config
from flask_sqlalchemy import SQLAlchemy 
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

from models import Article, Tag

@app.route('/')
def index():
	pagination = Article.query.order_by(Article.id.desc()).pagination(1, 
		per_page = config.MYBLOG_ARTICLE_PER_PAGE, error_out = False)
	return render_template('index.html', pagination = pagination)