from models import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(105), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())