from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Shirt(db.Model):
    shirt_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(150), nullable=False)
    primary_color = db.Column(db.String(150), nullable=False)
    secondary_color = db.Column(db.String(150), nullable=True)
    type = db.Column(db.Integer, nullable=False)
    times_worn = db.Column(db.Integer, nullable=False)
    last_time_worn = db.Column(db.String(50), default=func.now())
    worn_to_most = db.Column(db.String(50))
    user_id = db.Column(db.String(50))

class Pants(db.Model):
    pants_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(150), nullable=False)
    primary_color = db.Column(db.String(150), nullable=False)
    secondary_color = db.Column(db.String(150), nullable=True)
    type = db.Column(db.String(50), nullable=False)
    times_worn = db.Column(db.Integer, nullable=False)
    last_time_worn = db.Column(db.String(50), default=func.now())
    worn_to_most = db.Column(db.String(50))
    user_id = db.Column(db.String(50))

class Pants_Type(db.Model):
    pants_typeID = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))

class Shoes(db.Model):
    shoes_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(150), nullable=False)
    primary_color = db.Column(db.String(150), nullable=False)
    secondary_color = db.Column(db.String(150), nullable=True)
    type = db.Column(db.Integer, nullable=False)
    times_worn = db.Column(db.Integer, nullable=False)
    last_time_worn = db.Column(db.String(50), default=func.now())
    worn_to_most = db.Column(db.String(50))
    user_id = db.Column(db.String(50))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)