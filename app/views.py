from flask import *
from flask_login import *
from app import app
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
def index():
    user={"nickname":"chetan"} #random user
    posts=[#fake array of posts
            {
                'author':{'nickname':'Trickyman'},
                'body': 'In Delhi, it feels like the summer of 69....more like 69 degrees! :p
            },
            {
                'author':{'nickname':'AmyPal'},
                'body':'What is up with the USA?'
                }


            ]
    return render_template('index.html',
                           user=user,
                           posts=posts)

@app.route('/login',methods=['GET', 'POST'])
@oid.loginhandler
def login():
    #checking if g.user is set to an authenticated user, and in that case we redirect to the index page. g global is setup by Flask as a place to store and share data during the life of a request
    if g.user is not None and g.user .is_authenticated:
        return redirect(url_for('index')) #url_for is a a clean way to obtain the URL for a given view function

    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        session['remember_me']=form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname','email']) 

        return redirect('/index')
    return render_template('login.html',
                           title='Signin',
                           form = form,
                           providers=app.config['OPENID_PROVIDERS'])

# function that loads a user from the database
@lm.user_loader  #this decorator is used to register this func. with Flask-Login
def load_user(id):
    return User.query.get(int(id))
