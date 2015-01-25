#!/bin/bash
sudo killall /usr/bin/python
#sudo service nginx stop
sudo gunicorn project.wsgi:application --log-file error_logs.log --bind 127.0.0.1:8001 &
