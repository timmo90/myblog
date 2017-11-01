# -*-coding: utf-8 -*-
# created by timmo on 2017/10/31

from myblog import app
import time

def format_datetime(dateobj):
	# return time.strftime('%Y-%m-%d %H:%M:%S', dateobj)
	return dateobj.strftime('%Y-%m-%d %H:%M:%S')

app.jinja_env.globals['format_datetime'] = format_datetime
# app.add_template_global(format_datetime, 'format_datatime')