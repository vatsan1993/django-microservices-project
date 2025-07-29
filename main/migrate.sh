#!/bin/sh
echo "Waiting for MySQL..."
# while ! nc -z db 3306; do
#   sleep 1
# done
echo "MySQL started"
if [ ! -d "migrations" ]; then
  flask db init


fi
flask db migrate
flask db upgrade
# exec flask run --host=0.0.0.0 --port=5000
