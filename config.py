"""import modules"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisismysecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
    or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # taking the database url from the database_url environment variable,
    # and if that isnt defined, configure a database named app.db located
    # in the main directory which is stored in basedir variable.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ('MAIL_USE_TLS') is not None
    MAIL_USERNAAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['mugoiri@example.com']
    POSTS_PER_PAGE = 25
	LANGUAGES = ['en', 'es']
