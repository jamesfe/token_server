from __future__ import (absolute_import, division, print_function, unicode_literals)

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import token_config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = token_config.SQL_STR
db = SQLAlchemy(app)