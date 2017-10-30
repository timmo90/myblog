# -*-coding: utf-8 -*-
# created by timmo on 2017/10/29

from flask import Flask 
import config
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/hello')
def hello():
	return 'hello'