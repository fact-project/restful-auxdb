#!/bin/bash

service nginx start
cd /var/www/auxservice-www
gunicorn -k eventlet -b "127.0.0.1:5000" "auxservice:app"
