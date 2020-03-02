from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blogapp.config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config.from_object(Config)

from blogapp import routes, models

