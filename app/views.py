from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user={"nickname":"chetan"} #random user
    posts=[#fake array of posts
            {
                'author':{'nickname':'Jonah'},
                'body': 'In Delhi, it feels like the summer of 69'
            },
            {
                'author':{'nickname':'Amy'},
                'body':'What is up with the USA?'
                }
            
                
            ]
    return render_template('index.html',
                           user=user,
                           posts=posts)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Signin',
                           form = form)

