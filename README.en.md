# TaskFlow Django

A beginner-friendly project and task management CRUD application built with Django and server-side rendering.

## Features
- Authentication and dashboard
- Project and task CRUD
- Status, priority, and due dates
- Search and filtering
- Django Admin
- Tests and CI

## Stack
- Python 3.12+
- Django 5.2
- Django Templates
- PostgreSQL / SQLite

## Run locally

```bash
python -m venv .venv
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
