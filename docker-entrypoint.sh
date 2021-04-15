#!/bin/bash

echo "America/Recife" > /etc/timezone
dpkg-reconfigure -f noninteractive tzdata

if [ ! $port ]; then
  echo "Port not set, setting at default 8000"
  port=8000
fi

if [ "$makemig" = true ] ; then
        echo "yes" | python3 manage.py makemigrations
fi

if [ "$migrate" = true ] ; then
        echo "yes" | python3 manage.py migrate
fi

python3 manage.py runserver 0.0.0.0:$port