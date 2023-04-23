from flask import Blueprint, request, jsonify, make_response
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from models import db
from models.user import Users
from validation.authentication import (
    validate_email, 
    validate_username, 
    validate_password, 
    validate_first_name, 
    validate_last_name
)

authentication = Blueprint('authentication', __name__)


def perform_login(user, response_message):
    login_user(user)

    response = make_response(
        jsonify({
            'message': response_message,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'firstName': user.first_name,
                'lastName': user.last_name
            }
        }))

    expires = datetime.now() + timedelta(days=7)
    response.set_cookie('user_id', str(user.id), httponly=True, secure=True, samesite='Strict', expires=expires)

    return response, 200


@authentication.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()

        # Define validation methods
        VALIDATION_METHODS = {
            'email': validate_email,
            'username': validate_username,
            'password': validate_password,
            'first_name': validate_first_name,
            'last_name': validate_last_name
        }

        # Validate request data
        for key, method in VALIDATION_METHODS.items():
            value = data.get(key)
            is_valid, message = method(value)
            if not is_valid:
                return jsonify({ 'message': message }), 400

        new_user = Users(
            username=data.get('username'),
            password=generate_password_hash(data.get('password')),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            created_at=datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        user_to_login = Users.query.filter_by(username=new_user.username).first()

        # Successful registration
        return perform_login(user_to_login, 'Welcome to TableTop!')
    
    except Exception as e:
        print(f'An exception occured: {e}')
        return jsonify({ 'message': 'Failed to register.' }), 500
    

@authentication.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        user = Users.query.filter_by(username=data.get('username')).first() or \
               Users.query.filter_by(email=data.get('email')).first()

        if not user or not check_password_hash(user.password, data.get('password')):
            return jsonify({'message': 'Invalid credentials.'}), 401

        # Successful login
        return perform_login(user, f'Welcome back {user.first_name}!')

    except Exception as e:
        print(f'An exception occured: {e}')
        return jsonify({ 'message': 'Failed to log in.' }), 500


@authentication.route('/logout', methods=['POST'])
@login_required
def logout():
    try:
        logout_user()

        response = make_response(jsonify({'message': 'Logged out successfully.'}))
        response.delete_cookie('user_id')

        return response, 200

    except Exception as e:
        print(f'An exception occurred: {e}')
        return jsonify({'message': 'Failed to log out.'}), 500


@authentication.route('/validate-user', methods=['GET'])
@login_required
def validate_user():
    return jsonify({ 'message': 'User successfully validated.' }), 200