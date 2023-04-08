from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from auth_routes import auth_routes
from models import db
import os

app = Flask(__name__)

# The load_dotenv() function will load the environmental variables from the .env file into the os.environ dictionary. 
# You can then access the environmental variables using os.environ.get('MY_VARIABLE').
load_dotenv()

database_uri = os.environ.get('DATABASE_URI')

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

# Initialize the SQLAlchemy instance with the Flask app
db.init_app(app)

# # Define a model for the database
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(25), nullable=False, unique=True)
#     password = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     first_name = db.Column(db.String(25), nullable=False)
#     last_name = db.Column(db.String(25), nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

@app.get('/')
def index():
    return 'The server is running.'


app.register_blueprint(auth_routes)

if __name__ == '__main__':
    app.run(debug=True)