from flask import request, jsonify
from models.booking_model import Booking
from database import get_bookings_collection


def add_booking():
    data = request.get_json()
    user_id = data.get('user_id')
    event_id = data.get('event_id')
    theater_id = data.get('theater_id')
    num_tickets = data.get('num_tickets')

    new_booking = Booking(user_id=user_id, event_id=event_id,
                          theater_id=theater_id, num_tickets=num_tickets)

    bookings_collection = get_bookings_collection()
    bookings_collection.insert_one(new_booking.to_dict())

    return jsonify({'message': 'Booking added successfully'}), 201


def get_bookings():
    bookings_collection = get_bookings_collection()
    # Exclude the '_id' field from the response
    bookings = list(bookings_collection.find({}, {'_id': 0}))
    return jsonify(bookings), 200
