from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from routes import routes
from models import db
import os

app = Flask(__name__)

# The load_dotenv() function will load the environmental variables from the .env file into the os.environ dictionary. 
# You can then access the environmental variables using os.environ.get('MY_VARIABLE').
load_dotenv()

database_uri = os.environ.get('DATABASE_URI')
jwt_secret = os.environ.get('JWT_SECRET')

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['JWT_SECRET_KEY'] = jwt_secret
jwt = JWTManager(app)

# Initialize the SQLAlchemy instance with the Flask app
db.init_app(app)

CORS(app, supports_credentials=True)

app.register_blueprint(routes)

@app.get('/')
def index():
    return 'The server is running.'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)