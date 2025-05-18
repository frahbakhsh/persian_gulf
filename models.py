from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

class Map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    text = db.Column(db.Text)
    year = db.Column(db.String(10))
    source = db.Column(db.String(200))
    image_url = db.Column(db.String(300))

    def __str__(self):
        return self.title

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    source = db.Column(db.String(150))

    def __str__(self):
        return self.source

class OrganizationPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization = db.Column(db.String(100))
    position = db.Column(db.Text)

    def __str__(self):
        return self.organization
