from pymongo import MongoClient
from config import MONGO_URI

# Connect to MongoDB and create a database connection


def get_db():
    client = MongoClient(MONGO_URI)
    db = client.cinetickets  # Use the desired database name 'cinetickets'
    return db

# Create collections for each entity


def get_users_collection():
    db = get_db()
    return db['users']


def get_movies_collection():
    db = get_db()
    return db['movies']


def get_admins_collection():
    db = get_db()
    return db['admins']


def get_events_collection():
    db = get_db()
    return db['events']


def get_theaters_collection():
    db = get_db()
    return db['theaters']


def get_bookings_collection():
    db = get_db()
    return db['bookings']
