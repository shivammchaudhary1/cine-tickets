from flask import Blueprint
from controllers.theater_controller import add_theater, get_theaters

theater_bp = Blueprint('theater_bp', __name__, url_prefix='/theaters')

# Route for adding a new theater


@theater_bp.route('/add', methods=['POST'])
def add():
    return add_theater()

# Route for getting all theaters


@theater_bp.route('/', methods=['GET'])
def get_all():
    return get_theaters()
