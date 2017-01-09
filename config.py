import os


class Base(object):
    # Flask Config
    basedir = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    DEBUG = False
    ENV = os.environ['ENV']

    # SQLAlchemy Config
    DATABASE_QUERY_TIMEOUT = 0.5
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

    # TWILIO Config
    try:
        TWILIO_ACCOUNT_SID=os.environ['TWILIO_ACCOUNT_SID']
        TWILIO_ACCOUNT_AUTH=os.environ['TWILIO_ACCOUNT_AUTH']
    except KeyError:
        raise('Missing Twilio environ variables')

class STAGING(Base):
    DEBUG = True
    SECRET_KEY = 'Replace_With_SecretKey'
    DATABASE_QUERY_TIMEOUT = 1.0


class PRODUCTION(Base):
    SECRET_KEY = os.environ.get('SECRET_KEY', '')
