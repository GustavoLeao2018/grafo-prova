from random import randint

class Movie:
    """Implementa um objeto Movie, conectado a outros."""

    def __init__(self, title, genre, rating):
        """Inticializa o objeto Movie."""
        self._title = title
        self._genre = genre
        self._rating = rating
        self._similar = []
        self.coordenada = (randint(-300, 300), randint(-400, 400))

    def add_similar(self, movie):
        """Adiciona um Movie similar a lista de similares."""
        self.similar.append(movie)

    @property
    def title(self):
        return self._title

    @property
    def genre(self):
        return self._genre

    @property
    def rating(self):
        return self._rating

    @property
    def similar(self) -> list:
        return self._similar

    @similar.setter
    def similar(self, new_value: list):
        self._similar = new_value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "%s (%s): %g" % (self._title, self._genre, self._rating)
