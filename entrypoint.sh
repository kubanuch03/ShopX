# Запуск Redis
apt update
apt install redis-server
redis-server --port 6379 &

# Ожидание запуска Redis (дополнительная команда, если необходимо)
sleep 5

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
#gunicorn Shopx.wsgi:application --bind 0.0.0.0:8001 --workers 4 --timeout 60
#daphne -b 0.0.0.0 -p 8000 Shopx.asgi:application
# Запускаем Celery worker
celery -A Shopx worker --loglevel=info --detach

# Запускаем Celery beat
celery -A Shopx beat --loglevel=info --detach

# Ожидаем завершения Gunicorn (или любого другого процесса, запущенного перед)
wait -n


