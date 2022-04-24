import os

class Config(object):
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
#    SECRET_KEY = os.environ.get('SECRET_KEY') or 'do-or-do-not-there-is-no-try'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/lu-ms1-products_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False