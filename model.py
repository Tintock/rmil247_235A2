


class Actor:
    
    def __init__(self, actor_full_name : str):
        if actor_full_name  == "" or type(actor_full_name) is not str:
            self.__actor_full_name  = None
        else:
            self.__actor_full_name  = actor_full_name .strip()
        self.colleagues = []
    
    def add_actor_colleague(self, other):
        if isinstance(other, Actor) == True and self.check_if_this_actor_worked_with(other) == False:
            self.colleagues.append(other)
            other.add_actor_colleague(self)
        else:
            pass
    def check_if_this_actor_worked_with(self, colleague):
        try:
            if colleague in self.colleagues:
                return True
            else:
                return False
        except:
            return False
        
    @property
    def actor_full_name (self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name }>"

    def __eq__(self, other):
        if self.__actor_full_name == other:
            return True
        elif self.__actor_full_name != other:
            return False

    def __lt__(self, other):
        try:
            if self.actor_full_name  <= other.actor_full_name :
                return True
            else:
                return False
        except TypeError:
            return False
        
    def __hash__(self):
        return hash((self.actor_full_name))
        

class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if self.__director_full_name == other:
            return True
        elif self.__director_full_name != other:
            return False

    def __lt__(self, other):
        try:
            if self.director_full_name <= other.director_full_name:
                return True
            else:
                return False
        except TypeError:
            return False

    def __hash__(self):
        return hash((self.director_full_name))


class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if self.__genre_name == other:
            return True
        elif self.__genre_name != other:
            return False

    def __lt__(self, other):
        try:
            if self.genre_name <= other.genre_name:
                return True
            else:
                return False
        except TypeError:
            return False

    def __hash__(self):
        return hash((self.genre_name))

class Movie:
    
    def __init__(self, _title: str, year: int):
        if _title == "" or type(_title) is not str:
            self.__title = None
        else:
            self.__title = _title.strip()
        
        if year == "" or type(year) is not int or year < 1900:
            self.__year = None
        else:
            self.__year = year
            
        self.__director = None
        self.__runtime_minutes = None
        
        self.__actors = []
        self.__genres = []
        
        self.__description =""
        
    @property
    def title(self) -> str:
        return self.__title
    @property
    def release_year(self) -> int:
        return self.__year
    
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, x: str):        
        if x == "" or type(x) is not str:
            self.__description = None
        else:
            self.__description = x.strip()
    
    @property
    def director(self):
        return self.__director
    @director.setter
    def director(self, x):
        if type(x) is Director:
            self.__director = x
        else:
            pass
    
    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes
    
    
    @runtime_minutes.setter
    def runtime_minutes(self, x):
        if type(x) is int and x>0:
            self.__runtime_minutes = x
        else:
            raise ValueError
            
            
    @property
    def actors(self):
        return self.__actors
    
    def add_actor(self, actor):
        if actor not in self.__actors and type(actor) is Actor:
            self.__actors.append(actor)
        else:
            pass
        
    def remove_actor(self, actor):
        try:
            self.__actors.remove(actor)
        except:
            pass
        
    @property
    def genres(self):
        return self.__genres
    
    def add_genre(self, genre):
        if genre not in self.__genres and type(genre) is Genre:
            self.__genres.append(genre)
        else:
            pass
        
    def remove_genre(self, genre):
        try:
            self.__genres.remove(genre)
        except:
            pass
    

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        return ((self.__title, self.__year) == (other.title, other.release_year))

    def __lt__(self, other):
        return ((self.__title, self.__year) < (other.title, other.release_year))
        
    def __hash__(self):
        return hash((self.__title, self.__year))
    
    
class Review:
    
    def __init__(self, movie = None, review_text = None, rating = None, timestamp = None):
        if type(movie) is Movie:
            self._movie = movie
        else:
            self._movie = None
        if type(review_text) is str:
            self._review_text = review_text.strip()
        else:
            self._review_text = None
        if type(rating) is int and 1 <= rating <= 10:
            self._rating = rating
        else:
            self._rating = None
        if type(timestamp) is datetime:
            self._timestamp = timestamp
        else:
            self._timestamp = None
    @property
    def movie(self):
        return self._movie
    @movie.setter
    def movie(self, x):
        if type(x) is Movie:
            self._movie = x
        else:
            self._movie = None
        
    @property
    def review_text(self):
        return self._review_text
    @review_text.setter
    def review_text(self, s):
        if type(s) is str:
            self._review_text = s.strip()
        else:
            self._review_text = None
        
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, x):
        if type(x) is int and 1 <= x <= 10:
            self._rating = x
        else:
            self._rating = None
        
    @property
    def timestamp(self):
        return self._timestamp
    @timestamp.setter
    def timestamp(self, t):
        if type(t) is datetime:
            self._timestamp = t
        else:
            self._timestamp = None
      
    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"
    def __eq__(self, other):
        return((self._movie, self._review_text, self._rating, self._timestamp) == (other._movie, other._review_text, other._rating, other._timestamp))


class User:

    def __init__(self, user_name: str, password: str):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password
        self.__watched_movies = list()
        self.__reviews = list()
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    def watch_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        if isinstance(review, Review):
            self.__reviews.append(review)

    def __repr__(self):
        return f'<User {self.__user_name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.user_name == self.__user_name

    def __lt__(self, other):
        return self.__user_name < other.user_name

    def __hash__(self):
        return hash(self.__user_name)


