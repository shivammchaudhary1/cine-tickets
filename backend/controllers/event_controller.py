from flask import request, jsonify
from models.event_model import Event
from database import get_events_collection


def add_event():
    data = request.get_json()
    name = data.get('name')
    date = data.get('date')
    location = data.get('location')
    description = data.get('description')

    new_event = Event(name=name, date=date, location=location,
                      description=description)

    events_collection = get_events_collection()
    events_collection.insert_one(new_event.to_dict())

    return jsonify({'message': 'Event added successfully'}), 201


def get_events():
    events_collection = get_events_collection()
    # Exclude the '_id' field from the response
    events = list(events_collection.find({}, {'_id': 0}))
    return jsonify(events), 200
