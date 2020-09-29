#!/bin/sh
echo "Waiting for postgres..."
while ! nc -z postgres 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

FLASK_ENV="development"
if [ "$FLASK_ENV"=="development" ]; then
  python manage.py run
else
  gunicorn -b 0.0.0.0:5000 manage:app
fi