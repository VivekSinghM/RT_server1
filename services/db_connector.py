from pymongo import MongoClient
import os
from app import app
from flask_sqlalchemy import SQLAlchemy

from constant import *

LOCAL_DATABASE_URL = SQL_URI[postgress]
app.config['SQLALCHEMY_DATABASE_URI'] = LOCAL_DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
db = SQLAlchemy()
db.app = app
db.init_app(app)


# Requires the PyMongo package.
# https://api.mongodb.com/python/current

# mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_client = MongoClient(NOSQL_URI[mongodb])

mongo_col = mongo_client['RTM']['Orders']
