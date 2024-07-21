# Flusk API

## Local environment python

```bash
# install virtual env
pip install virtualenv

# Create virtual env
virtualenv env

# Activate virtual env
source env/bin/activate

# Deactivate virtual env
deactivate

# change versi pythone
virtualenv -p python3 env

```

## Install Package

```bash
# install flask
pip install flask

# install flask migrate
pip install flask-migrate

# install dot env
pip install python-dotenv

# install sql alchemy
pip install flask-sqlalchemy

# install driver mysql
pip install pymysql
```

## Migrate DB

```bash
# initial database
flask db init

# create migrate database
flask db migrate -m "membuat table user"

# upgrade database
flask db upgrade
```

## Menjalankan APP

```bash
# running mode development
flask run
```