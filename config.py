import os

WTF_CSRF_ENABLED=True
SECRET_KEY = 'robin101!'

OPENID_PROVIDERS = [
 {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
                {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
                    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
                        {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
                            {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))

SQL_ALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')  #this path is our database file
SQL_ALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')   #this is the folder where i will store SQLAlchemy-migrate data files

