from flask import Blueprint, jsonify, request
from models.movie_model import create_movie, get_movie_by_id, get_movies_filter, update_movie

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
    order_by = request.args.get("order_by")
    desc = request.args.get("desc", False)

    movies = get_movies_filter(genre=genre, year_from=year_from, year_to=year_to, min_rating=min_rating, order_by=order_by, desc=desc)
    if not movies:
        return jsonify({"error": "No se encontraron peliculas con los filtros proporcionados"}), 404
    return jsonify(movies)

@movies_bp.route("/", methods=["POST"])
def add_movie():
    # Recibimos los datos como JSON
    data= request.json
    titulo= data.get("titulo")
    director= data.get("director")
    anio= data.get("anio")
    rating= data.get("rating")
    genero= data.get("genero")
    imagen= data.get("imagen")
    
    if not titulo or not director or anio is None:
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    if rating is None and rating not in (None, ""):
        return jsonify({"error": "El rating debe ser un numero"}), 400
    
    new_movie_id= create_movie(titulo, director, anio, rating, genero, imagen)
    return jsonify({"message": "Pelicula creada", "id": new_movie_id}), 201
    
@movies_bp.route("/<int:id>", methods=["PUT"])
def edit_movie(id):
    data = request.json
    titulo = data.get("titulo")
    director = data.get("director")
    anio = data.get("anio")
    rating = data.get("rating")
    genero = data.get("genero")
    imagen = data.get("imagen")

    if not titulo or not director or anio is None:
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    if rating is None and rating not in (None, ""):
        return jsonify({"error": "El rating debe ser un numero"}), 400

    update_movie(id, titulo, director, anio, rating, genero, imagen)
    return jsonify({"message": "Película actualizada"}), 200
# ...existing code...
