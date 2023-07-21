from flask import Blueprint
from controllers.event_controller import add_event, get_events

event_bp = Blueprint('event_bp', __name__, url_prefix='/events')

# Route for adding a new event


@event_bp.route('/add', methods=['POST'])
def add():
    return add_event()

# Route for getting all events


@event_bp.route('/', methods=['GET'])
def get_all():
    return get_events()
