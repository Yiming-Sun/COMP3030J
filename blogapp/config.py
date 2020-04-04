import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # SECRET_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'blogdb.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD = os.path.join(basedir, 'static\\upload_photo')
