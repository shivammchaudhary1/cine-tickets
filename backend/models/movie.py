# models/movie.py

from flask_mongoengine import Document
from mongoengine.fields import StringField, IntField, FloatField


class Movie(Document):
    title = StringField(required=True, max_length=100)
    Vposter = StringField(required=True)  # URL to vertical poster image
    Hposter = StringField(required=True)  # URL to horizontal poster image
    director = StringField(max_length=100)
    genre = StringField(max_length=50)
    language = StringField(max_length=50)
    duration = IntField()  # Duration in minutes
    year = IntField(min_value=1800, max_value=9999)
    rating = FloatField(min_value=0.0, max_value=10.0)
    desc = StringField()
