# user_routes.py
from flask import Blueprint, request, jsonify
from controllers.user_controller import register_user, login_user, get_user_details

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

# Route for user registration


@user_bp.route('/register', methods=['POST'])
def register():
    return register_user()

# Route for user login


@user_bp.route('/login', methods=['POST'])
def login():
    return login_user()

# Route for retrieving user details


@user_bp.route('/<string:user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_details(user_id)
