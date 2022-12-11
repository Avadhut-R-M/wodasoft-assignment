#!/bin/sh

psql postgres -c "CREATE USER myproject1user WITH PASSWORD 'password'"
psql postgres -c "ALTER ROLE myproject1user SET client_encoding TO 'utf8'"
psql postgres -c "CREATE DATABASE myproject1"
psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE myproject1 TO myproject1user"
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

