from flask import Blueprint, request, jsonify, make_response
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db
from models.user import Users
from routes.decorators import jwt_required_cookie

authentication = Blueprint('authentication', __name__)

# @authentication.get('/get-all-users')
# def get_all_users():
#     users = Users.query.all()
#     output = [ 
#         { key: getattr(user, key) for key in ['id', 'username', 'email', 'first_name', 'last_name', 'created_at'] } 
#         for user in users
#     ]
#     return jsonify(output)


@authentication.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    try:
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

        return jsonify({ 'message': 'User successfully registered.' }), 201
    
    except Exception as e:
        print(f'An exception occured: {e}')
        return jsonify({ 'message': 'The user could not be created.' }), 500
    

@authentication.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        user = Users.query.filter_by(username=data.get('username')).first() or \
               Users.query.filter_by(email=data.get('email')).first()

        if not user or not check_password_hash(user.password, data.get('password')):
            return jsonify({'message': 'Invalid credentials.'}), 401

        response = make_response(jsonify({'message': 'Logged in successfully.'}))

        token = create_access_token(identity=user.id)
        expires = datetime.now() + timedelta(days=7)
        response.set_cookie('token', token, httponly=True, secure=True, samesite='Strict', expires=expires)

        return response, 200

    except Exception as e:
        print(f'An exception occured: {e}')
        return jsonify({ 'message': 'The user could not be created.' }), 500


@authentication.route('/validate-user', methods=['POST'])
@jwt_required_cookie
def validate_user():
    current_user_id = get_jwt_identity()
    return jsonify(logged_in_as=current_user_id), 200