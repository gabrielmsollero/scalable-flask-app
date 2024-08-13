#!/usr/bin/env bash
cd ./deployment
service nginx start
uwsgi --ini uwsgi.ini