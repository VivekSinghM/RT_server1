from main import app
from flask_sqlalchemy import SQLAlchemy

from constant import *

app.config['SQLALCHEMY_DATABASE_URI']= SQL_URI[postgress]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

# mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_client = MongoClient('mongodb+srv://user1:HiwaW0Jo4eBNeJTD@cluster0.sydu8iv.mongodb.net/test')

mongo_col = mongo_client['RTM']['Orders']