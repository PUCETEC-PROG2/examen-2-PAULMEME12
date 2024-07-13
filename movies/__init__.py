class Movie:
    def __init__(self, title, genre, director, year, synopsis):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.synopsis = synopsis


movie1 = Movie("Título de la película", "Género de la Película", "Nombre del director", 2023, "Sinopsis de la película")

print(movie1.title)
print(movie1.genre)
print(movie1.director)
print(movie1.year)
print(movie1.synopsis)
