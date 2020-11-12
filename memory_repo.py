from movie_file_csv_reader import MovieFileCSVReader

"""can change this and the file reader and as long as it returns data, genre, director and actor as lists the app will work"""

def abstract():
    filename = 'Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    data = movie_file_reader.dataset_of_movies
    genre = movie_file_reader.dataset_of_genres
    director = movie_file_reader.dataset_of_directors
    actor = movie_file_reader.dataset_of_actors
    return data,genre,director,actor