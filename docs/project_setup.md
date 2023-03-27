## How to setup project?
1. Clone repository:
```
git clone https://github.com/lymagics/sheepfish-challenge.git
```
2. Create python virtual environment^
```
python -m venv [VENV_NAME]
[VENV_NAME]/Scripts/activate
```
3. Install project dependencies:
```
pip install -r requirements/development.txt
```
4. Fill in .env.services and src/.env files.
5. Run services:
```
docker-compose up -d
```
7. Change directory to src:
```
cd src
```
6. Run migrations:
```
python manage.py migrate
```
7. Create django superuser:
```
python manage.py createsuperuser
```
8. Go to admin panel and create interval for print_checks task.
9. Run celery worker and beat:
```
celery --app config.celery.app worker -l info
celery --app config.celery.app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler 
```
10. Run server:
```
python manage.py runserver
```