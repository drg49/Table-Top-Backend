import re
from models.user import Users

def validate_email(email):
    if len(email) < 3 or len(email) > 150:
        return False, 'Email address must be between 3 and 150 characters long.'
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, 'Invalid email address.'
    if Users.query.filter_by(email=email).first():
        return False, 'Email address already registered.'
    return True, ''

def validate_username(username):
    if len(username) < 3 or len(username) > 25:
        return False, 'Username must be between 3 and 25 characters.'
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, 'Username must only contain letters, numbers, and underscores.'
    if Users.query.filter_by(username=username).first():
        return False, 'Username already taken.'
    return True, ''

def validate_password(password):
    if len(password) < 3 or len(password) > 105:
        return False, 'Password must be between 3 and 105 characters long.'
    if ' ' in password:
        return False, 'Password cannot contain blank spaces.'
    return True, ''

def validate_first_name(first_name):
    if not first_name:
        return False, 'First name cannot be empty.'
    if not re.match(r'^[a-zA-Z]+(?: [a-zA-Z]+)?$', first_name):
        return False, 'First name can only contain letters and one space.'
    if len(first_name) > 25:
        return False, 'First name cannot be longer than 25 characters.'
    return True, ''

def validate_last_name(last_name):
    if not last_name:
        return False, 'Last name cannot be empty.'
    if len(last_name) > 25:
        return False, 'Last name cannot be longer than 25 characters.'
    if not re.match(r'^[a-zA-Z]+( [a-zA-Z]+){0,2}$', last_name):
        return False, 'Last name can only contain letters and at most two spaces.'
    return True, ''