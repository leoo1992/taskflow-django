# TaskFlow Django
CRUD iniciante de projetos e tarefas feito integralmente com Django e renderização server-side.

## Recursos
Autenticação, dashboard, CRUD de projetos, CRUD de tarefas, status/prioridade/prazo, busca/filtro, Django Admin, testes e CI.

## Stack
Python 3.12+, Django 5.2, Django Templates, HTML/CSS e PostgreSQL/SQLite.

## Local
```bash
python -m venv .venv
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Vercel
Configure SECRET_KEY, DEBUG=False, ALLOWED_HOSTS=.vercel.app e DATABASE_URL nas Environment Variables. Use PostgreSQL persistente para produção.