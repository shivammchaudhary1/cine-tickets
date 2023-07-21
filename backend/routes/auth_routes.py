# auth_routes.py
from flask import Blueprint
from controllers.auth_controller import login, logout, reset_password

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

# Route for user login


@auth_bp.route('/login', methods=['POST'])
def user_login():
    return login()

# Route for user logout


@auth_bp.route('/logout', methods=['POST'])
def user_logout():
    return logout()

# Route for resetting user password


@auth_bp.route('/reset_password', methods=['POST'])
def reset_user_password():
    return reset_password()
