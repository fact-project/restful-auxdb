#!/bin/bash

service nginx start
uwsgi --ini /var/www/auxservice-www/auxservice_uwsgi.ini &
touch  /var/log/uwsgi/auxservice_uwsgi.log
tail -f /var/log/uwsgi/auxservice_uwsgi.log
