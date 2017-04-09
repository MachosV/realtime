# Usimmonitor

For production deployment, clone or pull the deployment branch

Requirements

1)nginx

2)redis

3)gunicorn (inside the virtualenv of the project)

Steps:

$redis-server

$python manage.py collectstatic

$python manage.py runworker --only-channels=websocket.*

$daphne -b 127.0.0.1 -p 8001 realtime.asgi:channel_layer

$gunicorn realtime.wsgi:application

$nginx
