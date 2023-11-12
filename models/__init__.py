from flask_sqlalchemy import SQLAlchemy

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

# Importing models here to prevent circular dependenceies
from .restaurant import Restaurant
from .category import Category
