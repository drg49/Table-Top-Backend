from flask import Blueprint, jsonify, make_response
from models import db
from flask_login import login_required
from models.restaurant import Restaurant

restaurant = Blueprint('restaurant', __name__)

@restaurant.route('/', methods=['GET'])
# @login_required
def get_restuarants():
    try:
        
        restaurants = Restaurant.query.all()
        
        # Convert the SQLAlchemy objects to a list of dictionaries
        restaurant_list = [
            {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "phone_number": restaurant.phone_number,
                "category_id": restaurant.category_id,
                "review_stars": float(restaurant.review_stars) if restaurant.review_stars is not None else None,
                "hours_of_operation": restaurant.hours_of_operation,
                "website_link": restaurant.website_link,
                "attributes": restaurant.attributes,
                "created_at": restaurant.created_at
            }
            for restaurant in restaurants
        ]

        # Return the list of restaurants as a JSON response
        return jsonify({"restaurants": restaurant_list}), 200

    except Exception as e:
        print(f'An exception occurred: {e}')
        return jsonify({'message': 'Failed to add reservation.'}), 500

