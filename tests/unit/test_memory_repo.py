from memory_repo import abstract
import pytest

@pytest.fixture()
def movie():
    data_file,genre_file, director_file,actor_file, = abstract()
    return data_file

@pytest.fixture()
def genre():
    data_file,genre_file, director_file,actor_file, = abstract()
    return genre_file

@pytest.fixture()
def director():
    data_file,genre_file, director_file,actor_file, = abstract()
    return director_file

@pytest.fixture()
def actor():
    data_file,genre_file, director_file,actor_file, = abstract()
    return actor_file

def test_files(movie):
    assert movie[0].title == "Guardians of the Galaxy"
    assert movie[0].genre == ["Adventure","Mystery","Sci-Fi"]
    assert movie[0].director == "James Gunn"