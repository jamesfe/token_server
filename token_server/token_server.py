"""
A server that serves tokens for the gathering of social media.
Twitter: @jimmysthoughts
GitHub: github.com/jamesfe
"""
from __future__ import (absolute_import, division, print_function, unicode_literals)

from flask_app import app, db
from models import *

# What are some actions people can do?
# insert a new key
# log a request
# remove a key

if __name__ == '__main__':
    app.run()
