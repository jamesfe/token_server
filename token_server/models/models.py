from __future__ import (absolute_import, division, print_function, unicode_literals)

from flask_app import db


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    use_period_secs = db.Column(db.Integer)
    max_uses = db.Column(db.Integer)
    token_uses = db.relationship('TokenUsage', backref='token',
                                 lazy='dynamic')


class TokenUsage(db.Model):
    usage_application = db.Column(db.String(128))
    usage_timestamp = db.Column(db.DateTime)
    token_id = db.Column(db.Integer, db.ForeignKey('token.id'))
    id = db.Column(db.Integer, primary_key=True)


class FlickrToken(Token):
    __tablename__ = 'flickr_token'
    __mapper_args__ = {'polymorphic_identity': 'flickr_token'}
    id = db.Column(db.Integer, db.ForeignKey('token.id'), primary_key=True)
    application = db.Column(db.String(128))
    secret = db.Column(db.String(128))
    username = db.Column(db.String(128))


class InstagramToken(Token):
    __tablename__ = 'instagram_token'
    __mapper_args__ = {'polymorphic_identity': 'instagram_token'}
    id = db.Column(db.Integer, db.ForeignKey('token.id'), primary_key=True)
    client = db.Column(db.String(128))
    token_string = db.Column(db.String(128), unique=True)
    application = db.Column(db.String(128))
    secret = db.Column(db.String(128))
    username = db.Column(db.String(128))