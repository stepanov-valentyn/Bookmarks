__author__ = 'gareth'
from datetime import datetime

from sqlalchemy import desc
from Bookmarks import db


class Bookmarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    @staticmethod
    def newest(num):
        return Bookmarks.query.order_by(desc(Bookmarks.date)).limit(num)

    def __repr__(self):
        return "<Bookmarks '{}' : '{}'>".format(self.desctription, self.url)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    bookmarks = db.relationship('Bookmarks',backref='user',lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username