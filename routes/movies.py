from flask import Blueprint, jsonify, request
from models.movie_model import get_movie_by_id, get_movies_filter

movies_bp = Blueprint("movies", __name__)
    
@movies_bp.route("/<int:id>", methods=["GET"])
def get_movie(id):
    movie = get_movie_by_id(id)
    if not movie:
        return jsonify({"error": "Pelicula no encontrada"}), 404
    return jsonify(movie)

@movies_bp.route("/", methods=["GET"])
def get_movies_by_filter():
    genre = request.args.get("genre")
    year_from = request.args.get("year_from")
    year_to = request.args.get("year_to")
    min_rating = request.args.get("min_rating")

    movies = get_movies_filter(genre=genre, year_from=year_from, year_to=year_to, min_rating=min_rating)
    if not movies:
        return jsonify({"error": "No se encontraron peliculas con los filtros proporcionados"}), 404
    return jsonify(movies)
