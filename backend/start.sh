#!/bin/bash

if [ "$DEBUG" == True ]; then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic --no-input
    
    cp -r /app/static/. /backend_static/static/

    if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
        python manage.py createsuperuser \
            --no-input \
            --email "$DJANGO_SUPERUSER_EMAIL"
    fi
fi

gunicorn core.wsgi:application --bind 0:8000
