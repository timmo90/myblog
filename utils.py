# -*-coding: utf-8 -*-
# created by timmo on 2017/10/31

from myblog import app
import time

def format_datetime(dateobj):
	return time.strftime('%Y-%m-%d %H:%M:%S', dateobj)

app.jinja_env_globals['format_datetime'] = format_datetime