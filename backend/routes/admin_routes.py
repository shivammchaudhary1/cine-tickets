# admin_routes.py
from flask import Blueprint
from controllers.admin_controller import add_admin, remove_admin, update_admin

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

# Route for adding an admin


@admin_bp.route('/add', methods=['POST'])
def add_admin_route():
    return add_admin()

# Route for removing an admin


@admin_bp.route('/remove', methods=['POST'])
def remove_admin_route():
    return remove_admin()

# Route for updating admin details


@admin_bp.route('/update', methods=['POST'])
def update_admin_route():
    return update_admin()
