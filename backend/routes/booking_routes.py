from flask import Blueprint
from controllers.booking_controller import add_booking, get_bookings

booking_bp = Blueprint('booking_bp', __name__, url_prefix='/bookings')

# Route for adding a new booking


@booking_bp.route('/add', methods=['POST'])
def add():
    return add_booking()

# Route for getting all bookings


@booking_bp.route('/', methods=['GET'])
def get_all():
    return get_bookings()
