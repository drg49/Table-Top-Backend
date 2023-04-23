import re
from models.user import Users

def validate_email(email):
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
