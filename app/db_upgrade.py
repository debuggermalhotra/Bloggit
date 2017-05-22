#script for database upgrading
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY-DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
v=api.db_version(SQLALCHEMY_DATABSE_URI,SQLALCHEMY_MIGRATE_REPO)
print("Current database version: " + str(v))
