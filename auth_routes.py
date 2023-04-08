from flask import Blueprint, request, jsonify, make_response
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Users

auth_routes = Blueprint('routes', __name__)

@auth_routes.get('/get-all')
def get_all():
    users = Users.query.all()
    output = [ 
        { key: getattr(user, key) for key in ['id', 'username', 'email', 'first_name', 'last_name', 'created_at'] } 
        for user in users
    ]
    return jsonify(output)


@auth_routes.route('/register', methods=['POST'])
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
    

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = Users.query.filter_by(username=data.get('username')).first() or \
           Users.query.filter_by(email=data.get('email')).first()

    if not user or not check_password_hash(user.password, data.get('password')):
        return jsonify({'message': 'Invalid credentials.'}), 401

    response = make_response(jsonify({'message': 'Logged in successfully.'}))

    token = user.generate_token()
    expires = datetime.now() + timedelta(days=7)
    response.set_cookie('access_token', token, httponly=True, secure=True, expires=expires)

    return response, 200