# VARIABLES
#------------------------------------------
MANAGE = python manage.py

run:
	uvicorn main:app --reload

migrate:
	alembic upgrade head

migrations:
	alembic revision --autogenerate -m "initial"

mm:
	migrate
	migrations
