from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import *
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)


class TopTenTopic(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rank = db.Column(db.Integer, unique = True)
    url = db.Column(db.String(127))
    title = db.Column(db.String(127))
    avatar = db.Column(db.String(127))

    def __init__(self, rank, url, title, avatar):
        self.rank = rank
        self.url = url
        self.title = title
        self.avatar = avatar


class Pattern(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    input = db.Column(db.String(255), unique = True)
    output = db.Column(db.String(255))

    def __init__(self, input, output):
        self.input = input
        self.output = output


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(127), unique=True)
    title = db.Column(db.String(127))
    avatar = db.Column(db.String(127))
    start = db.Column(db.Date)
    end = db.Column(db.Date)
    view = db.Column(db.Integer)
    reply = db.Column(db.Integer)
    pri = db.Column(db.Integer)

    def __init__(self, ssM, ssD, stM, stD, title, url, avatar, view, reply):
        year = datetime.datetime.now().year
        self.start = datetime.date(year=year, month=ssM, day=ssD)
        self.end = datetime.date(year=year, month=stM, day=stD)
        self.title = title
        self.url = url
        self.avatar = avatar
        self.view = view
        self.reply = reply
        self.pri = reply * 10 + view

class Link:
    """class fit wechat's link format"""
    def __init__(self, title, desc, picUrl, url):
        self.title = title
        self.desc = desc
        self.picUrl = picUrl
        self.url = url


def init():
    db.create_all()

if __name__ == '__main__':
    init()