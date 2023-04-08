from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from routes import routes
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

app.register_blueprint(routes)

@app.get('/')
def index():
    return 'The server is running.'


if __name__ == '__main__':
    app.run(debug=True)