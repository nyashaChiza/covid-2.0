from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email  = db.Column(db.String(50))
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    initial =  db.Column(db.String(50))
    password  = db.Column(db.String(50))
    userType = db.Column(db.String(50), default='client')


class Institutions(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name  = db.Column(db.String(50))
    province  = db.Column(db.String(50))
    city  = db.Column(db.String(50))
    capacity = db.Column(db.Integer)
    contact =  db.Column(db.String(50))
    address = db.Column(db.String(150))
