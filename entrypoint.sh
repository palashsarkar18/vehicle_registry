#!/bin/sh

# Apply database migrations
python manage.py migrate

# Start the Django server
exec python manage.py runserver 0.0.0.0:8000
