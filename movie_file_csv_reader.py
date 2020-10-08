import csv

from model import Actor, Director, Movie, Genre

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []
    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            
            """index = 0"""
            for row in movie_file_reader:
                title = row['Title']
                
                release_year = int(row['Year'])
                actors = row['Actors']
                
                movie = Movie(title, release_year)
                movie.description = row['Description']
                for actor in actors.split(","):

                    actor = Actor(actor)
                    movie.add_actor(actor)
                    self.__dataset_of_actors.append(actor)
                    for x in actors:
                        actor.add_actor_colleague(x)
                
                a_genre = row['Genre']
                
                for genre in a_genre.split(","):
                    genre = Genre(genre)
                    movie.add_genre(genre)
                    self.__dataset_of_genres.append(genre)
                a_director = row['Director']
                
                director1 = Director(a_director)
                self.__dataset_of_directors.append(director1)
                
                movie.director = director1 
                
                
                """print(f"Movie {index} with title: {title}, release year {release_year}")"""
                """index += 1"""
                
                
                self.__dataset_of_movies.append(movie)
        self.__dataset_of_actors = set(self.__dataset_of_actors)
        self.__dataset_of_genres = set(self.__dataset_of_genres)
        self.__dataset_of_directors  = set(self.__dataset_of_directors)
        
    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies
    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors
    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors
    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

"""filename = 'Data1000Movies.csv'
movie_file_reader = MovieFileCSVReader(filename)
movie_file_reader.read_csv_file()

print(movie_file_reader.dataset_of_movies[2].description)"""
