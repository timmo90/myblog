# -*-coding: utf-8 -*-
# created by timmo on 2017/10/29
# the method to use this module is 'python manage.py shell'

# from myblog import app, db
# from models import Article, Tag #it's necessary to import object

# with app.app_context():
# 	db.drop_all()
# 	db.create_all()

# from myblog import db
# from models import Article, Tag
# import forgery_py
# from random import seed, randint
# from datetime import datetime

# def generate_fake_data(count):
# 	seed()

	# tags = ['python', 'java', 'php', 'javascript', 'sql', 'c++']
	# for t in tags:
	# 	tag = Tag(t)
	# 	db.session.add(tag)

	# db.session.commit()

# 	for i in range(count):
# 		title = forgery_py.lorem_ipsum.title()
# 		summary = forgery_py.lorem_ipsum.sentence()
# 		content = forgery_py.lorem_ipsum.paragraph()
# 		pub_time = datetime.now
# 		tag = Tag.query.offset(randint(0, Tag.query.count() - 1)).first().name
# 		article = Article(title, summary, content, [tag])

# if __name__ == '__main__':
# 	generate_fake_data(50)
# 	print 'generate fake data sucessful' 