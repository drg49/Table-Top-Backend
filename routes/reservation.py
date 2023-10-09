from flask import Blueprint, jsonify, make_response
from models import db
from flask_login import login_required
from models.reservation import Reservation

reservation = Blueprint('reservation', __name__)

@reservation.route('/add-reservation', methods=['POST'])
# @login_required
def add_reservation():
    try:
        
        response = make_response(jsonify({'message': 'Reservation added.'}))
        return response, 200

    except Exception as e:
        print(f'An exception occurred: {e}')
        return jsonify({'message': 'Failed to add reservation.'}), 500

