# Запуск Redis
<<<<<<< HEAD

=======
apt update
>>>>>>> e289b7570f0bcfeb760f1748f686c33f005fbb82
apt install redis-server
redis-server --port 6379 &

# Ожидание запуска Redis (дополнительная команда, если необходимо)
<<<<<<< HEAD
sleep 6

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000 --noasgi
# gunicorn Shopx.wsgi:application --bind 0.0.0.0:8000 --noasgi --workers 4 --timeout 60
=======
sleep 5

python manage.py migrate --noinput
python manage.py collectstatic --noinput
# python manage.py runserver 0.0.0.0:8000
gunicorn Shopx.wsgi:application --bind 0.0.0.0:8000 --noasgi --workers 4 --timeout 60
>>>>>>> e289b7570f0bcfeb760f1748f686c33f005fbb82
daphne -b 0.0.0.0 -p 8001 Shopx.asgi:application
# Запускаем Celery worker
celery -A Shopx worker --loglevel=info --detach

# Запускаем Celery beat
celery -A Shopx beat --loglevel=info --detach

# Ожидаем завершения Gunicorn (или любого другого процесса, запущенного перед)
wait -n


<<<<<<< HEAD

=======
>>>>>>> e289b7570f0bcfeb760f1748f686c33f005fbb82
