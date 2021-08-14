# Django

Commands work on django on command line
**Run app**
```shell
# 8080 to specific the port to open the server 
python manage.py runserver 8080
```
**Create app**
```shell
python manage.py startapp polls
```
**Apply database setting at mysite/settings.py**
```shell
python manage.py migrate
```
**Apply models changings**
```shell
python manage.py makemigrations polls
```
**Play with API in shell**
```shell
python manage.py shell
```
**Create admin**
```shell
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```
**Run tests**
```shell
python manage.py test polls
```
**Tree of the basic Django**
```shell
├───mysite
│   │   db.sqlite3
│   │   manage.py
│   │
│   ├───mysite
│   │   │   .settings.py.un~
│   │   │   asgi.py
│   │   │   settings.py
│   │   │   settings.py~
│   │   │   urls.py
│   │   │   wsgi.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           settings.cpython-39.pyc
│   │           urls.cpython-39.pyc
│   │           wsgi.cpython-39.pyc
│   │           __init__.cpython-39.pyc
│   │
│   └───polls
│       │   .admin.py.un~
│       │   .models.py.un~
│       │   .tests.py.un~
│       │   .urls.py.un~
│       │   .views.py.un~
│       │   admin.py
│       │   admin.py~
│       │   apps.py
│       │   models.py
│       │   models.py~
│       │   tests.py
│       │   tests.py~
│       │   urls.py
│       │   urls.py~
│       │   views.py
│       │   views.py~
│       │   __init__.py
│       │
│       ├───migrations
│       │   │   0001_initial.py
│       │   │   0002_auto_20210727_2233.py
│       │   │   __init__.py
│       │   │
│       │   └───__pycache__
│       │           0001_initial.cpython-39.pyc
│       │           0002_auto_20210727_2233.cpython-39.pyc
│       │           __init__.cpython-39.pyc
│       │
│       ├───static
│       │   └───polls
│       │       │   .style.css.un~
│       │       │   style.css
│       │       │   style.css~
│       │       │
│       │       └───images
│       │               background.gif
│       │
│       ├───templates
│       │   ├───admin
│       │   │       base_site.html
│       │   │
│       │   └───polls
│       │           .index.html.un~
│       │           detail.html
│       │           index.html
│       │           index.html~
│       │           results.html
│       │
│       └───__pycache__
│               admin.cpython-39.pyc
│               apps.cpython-39.pyc
│               models.cpython-39.pyc
│               tests.cpython-39.pyc
│               urls.cpython-39.pyc
│               views.cpython-39.pyc
│               __init__.cpython-39.pyc
│
└───secondsite
```

**Setting Oracle follow this blog: <https://github.com/aderayevans/blogs/blob/main/fix-ORA-65096-django.md>**
