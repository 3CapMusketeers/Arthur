#!/bin/sh
#echo "Waiting for postgres..."
#while ! nc -z postgres 5432; do
#  sleep 0.1
#done
#
#echo "PostgreSQL started"

gunicorn --config /usr/src/app/gunicorn_config.py manage:app