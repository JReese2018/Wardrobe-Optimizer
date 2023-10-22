from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Shirt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(150), nullable=False)
    primary_color = db.Column(db.String(150), nullable=False)
    secondary_color = db.Column(db.String(150), nullable=True)
    shirt_type = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Pants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(150), nullable=False)
    primary_color = db.Column(db.String(150), nullable=False)
    secondary_color = db.Column(db.String(150), nullable=True)
    pants_type = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Shoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(150), nullable=False)
    primary_color = db.Column(db.String(150), nullable=False)
    secondary_color = db.Column(db.String(150), nullable=True)
    shoes_type = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    shirts = db.relationship('Shirt')
    pants = db.relationship('Pants')
    shoes = db.relationship('Shoes')