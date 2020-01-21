web: cd mysite
web: pip install requirements.txt
web: python manage.py migrate
web: python manage.py runserver
web: gunicorn mysite.wsgi --log-file -
heroku ps:scale web=1
