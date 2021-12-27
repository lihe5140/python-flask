from app.extensions.init_sqlalchemy import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(20))
    rdatetime = db.Column(db.DateTime, default=datetime.now)
    rudatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username
