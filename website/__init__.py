from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# at some point you will want to make this an environment variable
app.config['SECRET_KEY'] = 'd0e4240e6fb74743016fed54800852f8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from website import routes