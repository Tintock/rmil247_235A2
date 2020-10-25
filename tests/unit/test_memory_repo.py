from memory_repo import abstract
import pytest

@pytest.fixture()
def movie():
    data_file,genre_file, director_file,actor_file, = abstract()
    return data_file


def test_files(movie, actor):
    assert movie[0].title == "Guardians of the Galaxy"
    assert movie[0].genre == ["Adventure","Mystery","Sci-Fi"]
    assert movie[0].director == "James Gunn"


"i dont get this :/ all my stuff is just buttons"