web:python manage.py runserver
web: gunicorn main.wsgi --log-file -
heroku ps:scale web=1
