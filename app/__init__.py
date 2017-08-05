import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

app=Flask(__name__)
app.config.from_object('config')  #telling flask to read and use config.py
db = SQLAlchemy(app)

lm=LoginManager()
lm.init_app(app)
lm.login_view='login'
oid=OpenID(app, os.path.join(basedir,'tmp'))  #flask-openid needs a apth to a temp folder where files can be stored

from app import views, models
