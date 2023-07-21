from flask import request, jsonify
from models.movie_model import Movie
from database import get_movies_collection


def add_movie():
    data = request.get_json()
    title = data.get('title')
    Vposter = data.get('Vposter')
    Hposter = data.get('Hposter')
    director = data.get('director')
    genre = data.get('genre')
    language = data.get('language')
    duration = data.get('duration')
    year = data.get('year')
    rating = data.get('rating')
    desc = data.get('desc')

    new_movie = Movie(title=title, Vposter=Vposter, Hposter=Hposter, director=director,
                      genre=genre, language=language, duration=duration, year=year, rating=rating, desc=desc)

    movies_collection = get_movies_collection()
    movies_collection.insert_one(new_movie.to_dict())

    return jsonify({'message': 'Movie added successfully'}), 201


def get_movies():
    movies_collection = get_movies_collection()
    # Exclude the '_id' field from the response
    movies = list(movies_collection.find({}, {'_id': 0}))
    return jsonify(movies), 200
