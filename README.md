# backend
A Django GraphQL (Graphene) base template

* Make sure your IDE/Editor has [Black](https://black.readthedocs.io/en/stable/editor_integration.html) and [EditorConfig](https://editorconfig.org/#pre-installed) plugins installed; and configure it lint file automatically when you edit/save.
* We use [Python Poetry](https://python-poetry.org) to manage depedencies
* `poetry install` will install all required depedencies
* `poetry shell` will activate virtualenv
* `poetry add <my-package>` to install mypackage from pypi
* `poetry export -f requirements.txt  > requirements.txt` to update requirements.txt file before deploying a new feature
* Make sure you run `pre-commit install` after the very first clone: https://pre-commit.com/

# SQL
```sql
CREATE ROLE my_username with encrypted password 'my_password';
ALTER ROLE my_username WITH LOGIN;
CREATE DATABASE my_db_name with owner my_username;
```
# Custom management commands

* `./manage.py choices_export` will update CHOICES.js and schema.graphql to the latest

# Future Updates
1. Django 4.0 Upgrade
2. Graphene 3 Upgrade (wait for django-graphene to support both Graphne 3 and Django 4)
3. User management in keycloak
