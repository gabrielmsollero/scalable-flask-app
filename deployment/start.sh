#!/usr/bin/env bash
cd ./deployment
sudo service nginx start
uwsgi --ini uwsgi.ini