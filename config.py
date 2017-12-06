# -*-cofing: urf-8 -*-
# created by timmo on 2017/10/29

SECRET_KEY = 'guest guest and guest again'
SQLALCHEMY_DATABASE_URI = 'mysql://root:feng@localhost:3306/myblog'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

MYBLOG_ARTICLE_PER_PAGE = 15

AUTHOR = 'Timmo'
CODE = '1234'

BASIC_AUTH_USERNAME = 'timmo'
BASIC_AUTH_PASSWORD = 'hello'
BASIC_AUTH_FORCE = True