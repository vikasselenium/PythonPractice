
class Movie:

    movie_id=1
    def __init__(self, title, year):
        self._title = title
        self._year = year
        self.movie_id=Movie.movie_id
        Movie.movie_id+=1

    def get_year(self):
        return self._year
    def set_year(self,new_year):
        self._year = new_year

    @property
    def title(self):
        print("calling getter method")
        return self._title

    @title.setter
    def title(self,new_title):
        print("Calling setter method")
        if isinstance(new_title,str) and new_title.isalpha():
            self._title= new_title
        else:
            raise ValueError("Title must be a string")

my_movie=Movie("My Movie", 1998)
#print(my_movie.get_year())
print(my_movie.title)

my_movie.title="MyNewMovie12"
print(my_movie.title)

