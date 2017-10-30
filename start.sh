rm -f *.pyc
sudo kill -9 `ps -aux | grep myblog_uwsgi | awk '{ print $2 }'`
sudo ln -sf /var/www/myblog/myblog_uwsgi.conf /etc/nginx/conf.d/myblog_uwsgi.conf
sudo mkdir -p /var/www/uwsgi-logs
sudo /etc/init.d/nginx restart
sudo chown mo:mo /var/www/myblog
sudo uwsgi --py-autoreload 1 --ini /var/www/myblog/myblog_uwsgi.ini --daemonize /var/www/uwsgi-logs/myblog_uwsgi.log
