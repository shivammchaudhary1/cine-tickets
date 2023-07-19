# database.py

from pymongo import MongoClient
from config import config

def connect_to_database():
    mongo_uri = config['MONGO_URI']
    client = MongoClient(mongo_uri)
    db = client.get_database('cinetickets')  # Replace with your database name
    return db
