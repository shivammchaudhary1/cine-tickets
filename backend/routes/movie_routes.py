from flask import Blueprint
from controllers.movie_controller import add_movie, get_movies

movie_bp = Blueprint('movie_bp', __name__, url_prefix='/movies')

# Route for adding a new movie


@movie_bp.route('/add', methods=['POST'])
def add():
    return add_movie()

# Route for getting all movies


@movie_bp.route('/', methods=['GET'])
def get_all():
    return get_movies()
