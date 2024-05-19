createsuperuser:
	python manage.py createsuperuser

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

start:
	gunicorn nasa.wsgi:application

runserver:
	python manage.py runserver

instpip:
	pip install -r req.pip

static_files:
	python manage.py collectstatic