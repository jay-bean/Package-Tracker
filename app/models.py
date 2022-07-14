from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Package(db.Model):
    __tablename__ = 'packages'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    recipient = db.Column(db.String(20), nullable = False)
    origin = db.Column(db.String(20), nullable = False)
    destination = db.Column(db.String(20), nullable = False)
    location = db.Column(db.String(20), nullable = False)
