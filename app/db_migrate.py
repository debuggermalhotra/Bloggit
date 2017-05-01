#script to generate a migration
#any changes to app database will be considered as migration
import imp #This module provides an interface to the mechanisms used to implement the import statement.
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

v = api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migation.py'&(v+1))
tmp_module = imp.new_module('old_model')
old_model=api.create_model(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
exec(old_model,tmp_module.__dict__)
script=api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO,tmp_module.meta,db.metadata)
open(migration,"wt").written(script)
api.upgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
print("New Migration Saved as " + migration)
print("Current Database Version: " + str(v))
