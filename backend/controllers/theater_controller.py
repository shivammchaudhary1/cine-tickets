from flask import request, jsonify
from models.theater_model import Theater
from database import get_theaters_collection


def add_theater():
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    capacity = data.get('capacity')

    new_theater = Theater(name=name, location=location, capacity=capacity)

    theaters_collection = get_theaters_collection()
    theaters_collection.insert_one(new_theater.to_dict())

    return jsonify({'message': 'Theater added successfully'}), 201


def get_theaters():
    theaters_collection = get_theaters_collection()
    # Exclude the '_id' field from the response
    theaters = list(theaters_collection.find({}, {'_id': 0}))
    return jsonify(theaters), 200
