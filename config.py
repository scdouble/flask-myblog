class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '\xa8\xcc\xeaP+\xb3\xe8 |\xad\xdb\xea\xd0\xd4\xe8\xac\xee\xfaW\x072@O3'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:password@localhost:15432/myblog"
