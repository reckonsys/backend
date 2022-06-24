# backend

A Django GraphQL (Graphene) base template

# Help?

Please ask your  questions in our #pythonista slack channel [and tag @dhilipsiva in the thread later]


# Prerequsites

* Refere to services sarted in [tmuxp.yaml](tmuxp.yaml)
* Create Postgres DB, USER: default creds can be found in `DATABASES` setting in [settings.py](https://github.com/reckonsys/backend/blob/develop/backend/settings.py) file
```sql
CREATE ROLE my_username with encrypted password 'my_password' LOGIN SUPERUSER;
CREATE DATABASE my_db_name with owner my_username;
```

# Development setup

1. Make sure you have `poetry` installed. We manage dependencies with it.
2. `poetry shell` inside backebd repo.
3. `poetry install` to update yours deps
4. `python manage.py migrate` to update your DB
5. `python manage.py runserver` to start the server.
6. `cp sample.env .env` to create a .env file and edit the Keys/Secrets/DSN as required.

This setup uses `sentry.io` and `uptrace.dev` services. Hence you should update the DSN in .env as required.

# Docs

* Make sure your IDE/Editor has [Black](https://black.readthedocs.io/en/stable/editor_integration.html) and [EditorConfig](https://editorconfig.org/#pre-installed) plugins installed; and configure it lint file automatically when you edit/save.
* We use [Python Poetry](https://python-poetry.org) to manage depedencies
* `poetry install` will install all required depedencies
* `poetry shell` will activate virtualenv
* `poetry add <my-package>` to install mypackage from pypi
* `poetry export -f requirements.txt  > requirements.txt` to update requirements.txt file before deploying a new feature
* Make sure you run `pre-commit install` after the very first clone: https://pre-commit.com/
* `./manage.py choices_export` will update CHOICES.js and schema.graphql to the latest
