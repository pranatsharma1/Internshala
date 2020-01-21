web:python manage.py runserver
web: gunicorn mysite.wsgi --log-file -
heroku ps:scale web=1
