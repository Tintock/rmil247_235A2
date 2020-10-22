"""app entry point"""
from flask import Flask, Blueprint, render_template
from model import Actor, Director, Movie, Genre, Review, User
from memory_repo import abstract
 
app = Flask(__name__)

data_file,genre_file, director_file,actor_file, = abstract()

home_blueprint = Blueprint(
    'home_bp', __name__)


@app.route("/")
@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home.html',
        movie_file = data_file
    )

browse_blueprint = Blueprint(
    'browse_bp', __name__)


@app.route("/browse")
@browse_blueprint.route('browse', methods=['GET'])
def browse():
    return render_template(
        'browse.html',
        movie_file = data_file
    )

genre_blueprint = Blueprint(
    'genre_bp', __name__)

@app.route("/genre")
@genre_blueprint.route('genre', methods=['GET'])
def genre():
    return render_template(
        'genre.html',
        movie_file = data_file,
        genres = genre_file
    )
director_blueprint = Blueprint(
    'director_bp', __name__)

@app.route("/director")
@director_blueprint.route('director', methods=['GET'])
def director():
    return render_template(
        'director.html',
        movie_file = data_file,
        directors = director_file
    )

actor_blueprint = Blueprint(
    'actor_bp', __name__)

@app.route("/actor")
@actor_blueprint.route('actor', methods=['GET'])
def actor():
    return render_template(
        'actor.html',
        movie_file = data_file,
        actors = actor_file
    )

search_blueprint = Blueprint(
    'search_bp', __name__)

@app.route("/search")
@search_blueprint.route('search', methods=['GET', 'POST'])
def search():
    return render_template(
        'search.html',
        movie_file = data_file,
        actors = actor_file,
        directors = director_file,
        genres = genre_file
    )

if __name__ == "__main__":
    app.run()