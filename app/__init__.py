from flask import Flask

app=Flask(__name__)
app.config.from_object('config')  #telling flask to read and use config.py


from app import views

