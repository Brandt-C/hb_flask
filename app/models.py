from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

#set up the sql table for users
class User(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(35), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(250), nullable=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    userpass = db.Column(db.String(30))


    def __init__(self, username, email, first_name, last_name, userpass, description=''):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name
        self.last_name = last_name
        self.id = str(uuid4())
        self.description = description
        self.userpass = userpass


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25))
    body = db.Column(db.String(255))
    geotag = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.String(50))

    def serialize(self):
        return {"id": self.id,
                'title': self.title,
                'body': self.body,
                'geotag': self.geotag,
                'timestamp': self.timestamp,
                'user_id' : self.user_id
                }



