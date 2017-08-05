import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED=True
SECRET_KEY = 'robin101!'

app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '1605033112901375',
        'secret': 'd39ff299df4ac9aa595c2ba25a0eff47'
    },
    'twitter': {
        'id': '5cFvfQOAuyneYKwCJ1wnBcOXl',
        'secret': 'HeTy1L4fLtZmnydcOyyOJYGCORzkpUDgSrpvF79QbXCG4KuEQ7'
    }
}


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')  #this path is our database file
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')   #this is the folder where i will store SQLAlchemy-migrate data files







OPENID_PROVIDERS = [
 {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
OPENID_PROVIDERS = [
 {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
                {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
                    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
                        {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
                            {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

                {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
                    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
                        {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
                            {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
