# Unisys Online

## Project Requirements
- Python 3.10.12
- Postgres 15.2

## Setup guide
**After the above mentioned technologies are installed & project is cloned, following is the procedure to start the project.**

1. Create `.env`  file in `globalexpress/` directory using `.env-sample`, values can be requested from administrator
2. Create & activate virtual enviornment:
    - `python -m venv name_of_venv`
    - Activate the virtual enviornemnt, the name of venv will show in start console line when activated
4. Install requirements
    - Use pip to install requirements from `requirements/`, run `pip install -r requirements/dev.txt`
5.  Do `python manage.py migrate` to run migrations and create database tables
6.  Install pre-commit by doing `pre-commit install` to enable automatic liniting on commits.



**Don't forget to migrate before running the command**
