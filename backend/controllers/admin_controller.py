# admin_controller.py
from flask import request, jsonify


def add_admin():
    # Implementation for adding an admin goes here
    data = request.get_json()
    # Your admin addition logic
    return jsonify({'message': 'Admin added successfully'}), 201


def remove_admin():
    # Implementation for removing an admin goes here
    data = request.get_json()
    # Your admin removal logic
    return jsonify({'message': 'Admin removed successfully'}), 200


def update_admin():
    # Implementation for updating admin details goes here
    data = request.get_json()
    # Your admin update logic
    return jsonify({'message': 'Admin details updated successfully'}), 200
