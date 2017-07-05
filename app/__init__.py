import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import basedir

app=Flask(__name__)
app.config.from_object('config')  #telling flask to read and use config.py
db = SQLAlchemy(app)

lm=LoginManager()
lm.init_app(app)
old=OpenId(app, os.path.join(basedir,'tmp'))

from app import views, models

