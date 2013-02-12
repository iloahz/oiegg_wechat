from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://oiegg:asdf1234@localhost:3306/oiegg'
db = SQLAlchemy(app)

class TopTenTopic(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rank = db.Column(db.Integer)
    url = db.Column(db.String(127))
    title = db.Column(db.String(255))
    avatar = db.Column(db.String(127))

    def __init__(self, rank, url, title, avatar):
        self.rank = rank
        self.url = url
        self.title = title
        self.avatar = avatar