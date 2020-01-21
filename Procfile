web: cd mysite
web: python manage.py runserver
web: gunicorn mysite.wsgi --settings=mysite.settings.production
heroku ps:scale web=1
