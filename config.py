import os


class Config():
    SECRET_KEY = os.urandom(2)


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'kaduk9393@gmail.com'
    MAIL_PASSWORD = 's7#Kasdf'
