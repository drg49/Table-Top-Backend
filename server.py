from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes import routes
from models import db
from flask_login import LoginManager
import os

app = Flask(__name__)

# The load_dotenv() function will load the environmental variables from the .env file into the os.environ dictionary.
# You can then access the environmental variables using os.environ.get('MY_VARIABLE').
load_dotenv()

database_uri = os.environ.get('DATABASE_URI')
jwt_secret = os.environ.get('JWT_SECRET')
login_manager = LoginManager()
login_manager.init_app(app)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SECRET_KEY'] = jwt_secret
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'

# Initialize the SQLAlchemy instance with the Flask app
db.init_app(app)

CORS(app, supports_credentials=True)

app.register_blueprint(routes)

@login_manager.user_loader
def load_user(user_id):
    from models.user import Users
    return Users.query.get(int(user_id))


@app.get('/')
def index():
    return 'The server is running.'
    
    
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
