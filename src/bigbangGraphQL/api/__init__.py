from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from bigbangGraphQL.config import CONFIG

app = Flask(__name__)
CORS(app)


# app.config["SQLALCHEMY_DATABASE_URI"] =  # CONFIG.uri_mysql
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
