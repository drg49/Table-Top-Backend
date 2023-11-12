from . import db
from flask_login import UserMixin

# In the context of this application, the term "user" pertains exclusively to individuals employed within the restaurant establishment. 
# It is noteworthy that customers are not required to register or establish accounts within this system.
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(105), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    def get_id(self):
        return str(self.id)
