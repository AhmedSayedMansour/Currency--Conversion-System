#!/bin/sh
echo ""
cat /opt/application/webapp/RELEASE
echo "------------------------------------------------"
echo "DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}"
echo "DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}"
echo "DJANGO_BIND_HOST=${DJANGO_BIND_HOST}"
echo "------------------------------------------------"
echo "Waiting for database ${MYSQL_USER}@${MYSQL_HOST}:${MYSQL_PORT}..."
while ! nc -z ${MYSQL_HOST} ${MYSQL_PORT}; do
  sleep 0.1
done
echo "Database ok"
echo "Collect static files..."
poetry run python manage.py collectstatic --no-input --clear --settings=base.settings.docker
ls -al /opt/application/webapp/staticfiles
# poetry run python manage.py makemigrations
echo "Migrate database..."
poetry run python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); user, created = User.objects.get_or_create(email='admin@admin.com', defaults={'is_staff': True, 'is_active': True, 'is_superuser': True, 'username': 'admin'}); (not created) or user.set_password('admin@123'); user.save()" | poetry run python manage.py shell -i python 
.venv/bin/gunicorn base.wsgi:application --bind ${DJANGO_BIND_HOST} --workers=1 --threads=4 --worker-class=gthread --worker-tmp-dir /dev/shm --timeout 180000
