from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = '123456789123'
app.config["MONGO_URI"] = "mongodb+srv://rahul:rahul4112@cluster0.1ukl56o.mongodb.net/task_db?retryWrites=true&w=majority"


# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes
