from flask import *
from flask_login import *
from app import app
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    user=g.user
    posts=[
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


# function that loads a user from the database
@lm.user_loader  #this decorator is used to register this func. with Flask-Login
def load_user(id):
    return User.query.get(int(id))


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


#since this function is decorated with befor_request, it will run before the view function each time a request is received
@app.befor_request
def befor_request():
    g.user=current_user #current_user global is set by Flask-Login

@oid.after_login
def after_login(resp): #resp contains the response/info. returned by OpenID provider
    #validating if email is provided or not
    if resp.email is None or resp.email == "":
        flash("Invalid login!! Try again.")
        return redirect(url_for('login'))
    #searching our database for the email
    user=User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname=resp.nickname
        if nickname is None or nickname="":
            nickname=User(nickname=nickname,email=resp.email)
            db.session.add(user)
            db.session.commit()
    remember_me=False
    #loading remember_me from flask session
    if 'remember_me' in session:
        remember_me=session['remember_me']
        session.pop('remember_me', None)
        login_user(user, remember=remember_me) #registering this is a valid login
        return redirect(request.args.get('next') or url_for('index'))
