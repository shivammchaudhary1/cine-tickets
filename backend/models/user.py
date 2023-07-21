# models/user.py

from flask_mongoengine import Document
from mongoengine.fields import StringField, IntField


class User(Document):
    name = StringField(required=True, max_length=100)
    age = IntField()
    email = StringField(required=True, unique=True)
    mobile = IntField()
    password = StringField(required=True)
