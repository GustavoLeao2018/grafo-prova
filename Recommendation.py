
from model import Movie
#database = "movies.csv"  # utilizado para avaliacao
database = "teste.csv"   # utilizado para testes

def recommend(source, count):
    recomendados = []
    c = 0
    maior = source.similar[0].rating
    for similar in source.similar:
        if similar.rating > maior:
            maior = similar.rating
    maior /= 2
    for similar in source.similar:
        if c < count:
            if similar.rating >= maior:
                recomendados.append(similar)
                c += 1
    return recomendados


def recommendInGenre(source, genre, count):
    recomendados = []
    c = 0
    maior = source.similar[0].rating
    for similar in source.similar:
        if similar.rating > maior:
            maior = similar.rating
    maior /= 2
    for similar in source.similar:
        if c < count:
            if similar.rating >= maior:
                if similar.genre == genre:
                    recomendados.append(similar)
                    c += 1
    return recomendados


def recommendCloser(source, maxDistance):
    recomendados = None
    c = 0
    maior = source.similar[0].rating
    for similar in source.similar:
        if similar.rating > maior:
            maior = similar.rating

    for similar in source.similar:
        if c <= maxDistance:
            if similar.rating >= maior:
                recomendado = similar
                c += 1
    return recomendado
    
