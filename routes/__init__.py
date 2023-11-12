from flask import Blueprint

# Import the route handlers from other files
from .authentication import authentication
from .restaurant import restaurant
from .reservation import reservation

# Create the blueprints
routes = Blueprint('routes', __name__)

# Register the blueprints with the Flask app
routes.register_blueprint(authentication, url_prefix='/authentication')
routes.register_blueprint(restaurant, url_prefix='/restaurants')
routes.register_blueprint(reservation, url_prefix='/reservation')
