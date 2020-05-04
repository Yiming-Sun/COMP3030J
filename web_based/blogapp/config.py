import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # SECRET_KEY
    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #'sqlite:///' + os.path.join(basedir, 'blogdb.db')
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PROT = 25
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "380777975@qq.com"
    MAIL_PASSWORD = "raxjmabnzywmcbef"
    MAIL_DEBUG = True

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACH_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:wywcj123@cdb-6jo4m3hi.bj.tencentcdb.com:10019/score'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD = os.path.join(basedir, 'static/upload_photo')
