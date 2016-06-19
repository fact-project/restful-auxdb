#!/bin/bash

service nginx start
uwsgi --ini /var/www/auxservice-www/auxservice_uwsgi.ini
