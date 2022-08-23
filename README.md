# PHONEBOOK

# Local development

## Requirements

- [Python 3.8](https://www.python.org/downloads/) or higher
- [pipenv](https://pypi.org/project/pipenv/) python module
- [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/)

## Run on local machine

Run DB with docker-compose

```shell script
docker-compose up -d
```

Install pipenv dependencies

```shell script
pipenv install --dev
```

Enter pipenv shell

```shell script
pipenv shell
```

Copy the `.env.example` file to `.env` and change configuration to appropriate values

```shell script
cp .env.example .env
```

Set up the database

```shell script
./manage.py migrate
```

Create a superuser

```shell script
./manage.py createsuperuser
```

Start the application locally

```shell script
./manage.py runserver
```
