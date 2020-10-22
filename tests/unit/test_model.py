from models import Actor, Director, Movie, Genre, Review, User

import pytest

@pytest.fixture()
def user():
    return User('testname', 'testsr2hard')

@pytest.fixture()
def movie():
    return Movie('Fake Movie 12', "test")

@pytest.fixture()
def actor():
    return Actor('Test Actor')

@pytest.fixture()
def genre():
    return Genre('Test')

@pytest.fixture()
def director():
    return Director('Test Director')

"""tests"""
def test_user_construction(user):
    assert user.user_name == 'testname'
    assert user.password == 'testsr2hard'
    assert repr(user) == '<User testname testsr2hard>'

def test_movie_construction(movie):
    assert movie.title =="Fake Movie 12"
    assert movie.release_year == None

def test_actor_construction(actor):
    assert actor.actor_full_name =="Test Actor"
    assert repr(actor) == "<Actor Test Actor>"

def test_genre_construction(genre):
    assert genre.genre_name == "Test"

def test_director_construction(director):
    assert director.director_full_name == "Test Director"

def test_full_movie_construction(movie):
    movie2 = Movie("Second Fake Movie", "2020")
    movie2.add_actor(actor)
    actor2 = Actor("Second Actor")
    movie2.add_actor(actor2)
    movie2.add_genre(genre)
    assert movie2.actors == ["<Actor Test Actor>", "<Actor Second Actor>"]
    assert movie2.genres == ["<Genre Test>"]
    assert movie2.__repr__ == "<Movie Second Fake Movie 2020>"