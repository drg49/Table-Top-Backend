from . import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    review_stars = db.Column(db.Numeric(3, 1))
    hours_of_operation = db.Column(db.String(255), nullable=False)
    website_link = db.Column(db.String(255))
    attributes = db.Column(db.JSON)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())

    category = db.relationship('Category', back_populates='restaurants')
