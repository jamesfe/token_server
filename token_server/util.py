from __future__ import (absolute_import, division, print_function, unicode_literals)
import json

from flask_app import db
from models import *


def load_keys(tgt_file):
    with open(tgt_file, 'r') as infile:
        in_data = infile.read()

    in_data = json.loads(in_data)
    for item in in_data:
        if item['application'] == 'flickr':
            new_token = FlickrToken(**item)
            db_insert_object(new_token)
        elif item['application'] == 'instagram':
            new_token = InstagramToken(**item)
            db_insert_object(new_token)


def db_insert_object(item):
    db.session.add(item)
    db.session.commit()
