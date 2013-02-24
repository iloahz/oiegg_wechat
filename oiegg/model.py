from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import *

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

class Link:
    """class fit the """
    def __init__(self, title, desc, avatar, url):


def init():
    db.create_all()

if __name__ == '__main__':
    init()