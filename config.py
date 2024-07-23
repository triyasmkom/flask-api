import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    PORT = str(os.environ.get("DB_PORT"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))


    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+USERNAME+':'+PASSWORD+'@'+HOST+":"+PORT+'/'+DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

