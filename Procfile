release: sh -c 'cd ./server && python manage.py makemigrations && python manage.py migrate && ls'
web: gunicorn --pythonpath server server.wsgi