#!/bin/sh
if [ ! -d "migrations" ]; then
  flask db init
fi
flask db migrate
flask db upgrade
exec flask run --host=0.0.0.0