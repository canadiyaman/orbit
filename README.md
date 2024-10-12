# Orbit Project
=================

![Badge](https://img.shields.io/badge/python-3.10.6-green.svg)
![Badge](https://img.shields.io/badge/django-5.1.2-green.svg)
![Badge](https://img.shields.io/badge/postgresql-14.13-blue.svg)



[Follow the link for documentation](documentation.md)

> Also postman collection is existed on the main directory with name Orbit.postman_collection.json

> [Click](https://www.postman.com/leepower/workspace/orbit/collection/2053445-b5be6e76-8be9-42c7-b509-6d47b3f0caae?action=share&creator=2053445) link to see online postman collection 

Installation
================

### 1. Manuel Setup

  - Install requirement libraries
  - Set .env file and fill it with necessary parameters
  - Run the migrations on base directory
  - Load initial data
  - Start the server
  ```properties
    pip install -r requirements.txt
    sudo cp .env-example .env
    python manage.py migrate
    python python manage.py createapiuser -username default & python manage.py loadinitialdata -c 500 -cn Work,Holiday,Gym,Family
    python manage.py runserver
  ```

### 2. Build with Docker

- Make sure you have Docker on your computer 
    https://www.docker.com/get-started/


- For Mac user needs to install docker-compose (I'm using home brew).
```properties
  brew install docker-compose
  docker compose up --build
```

- If you get connection error you may follow these steps. Or make sure all db credentials in 
.env file correctly

    ```properties
      docker compose down -v
      docker compose up --build
      docker compose exec db psql --username=orbit --dbname=orbit
        GRANT ALL PRIVILEGES ON DATABASE orbit TO orbit;
        ALTER USER orbit CREATEDB;
        ALTER USER orbit LOGIN;
    ```

    

Directory layout
================

Orbit's directory structure looks as follows::

    orbit/
    ├── orbit/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── routers.py
    │   ├── settings.py
    │   ├── urls.py    
    │   ├── wsgi.py
    └── event/
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   │── migrations
    │   │   └── 0001.initial.py
    │   ├── management/
    │   │   └──commands
    │   │       └── loadinitialdata.py
    │   ├── tests/
    │   │   ├── __init__.py
    │   │   ├── test_models.py
    │   │   └── test_views.py
    └── user/
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── models.py
    │   │── migrations
    │   │   └── 0001.initial.py
    │   ├── management/
    │   │   └──commands
    │   │       └── loadinitialdata.py
    └── .dockerignore
    └── .env-example
    └── .gitignore
    └── docker-compose.yml
    └── docker-entrypoint.sh
    └── Dockerfile
    └── documentation.md
    └── LICENCE
    └── manage.py
    └── Orbit.postman_collection.json
    └── pyproject.toml
    └── README.md
    └── requirements.txt
    └── tox.ini

Development
================

- Run and make sure all tests are running
  ```shell
  coverage run mnaage.py test
  ```

- Make sure you checked the code quality after any change using with following commands
    ```properties
    black .
    flake8 .
    ```
