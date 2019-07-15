
from random import *
import csv

import Recommendation
from model import Movie
from Desenha import *

def loadMovieDatabase(filename):
    """Le o banco de dados de filmes, no formato CSV."""
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, quotechar='"')
        movie_list = []
        edges = []
        for row in reader:
            title = row[0]
            genre = row[1]
            rating = float(row[2])
            movie_list.append(Movie(title, genre, rating))
            edges.append([int(row[i]) for i in range(3, len(row))])
        for i, movie in enumerate(movie_list):
            mvs = [movie_list[x] for x in edges[i]
                   if x < len(movie_list)]
            movie.similar = mvs

        return movie_list


movies = loadMovieDatabase(Recommendation.database)

src = choice(movies)
generos = []
for f in movies:
    generos.append(f.genre) 
genero = choice(generos) 
count = 5
distancia = 5

Desenha().desenhar(movies)


for f in movies:
    if f  == src:
        print(f)
        for similar in f.similar:
            print('\t',similar)

print('*'*100)
print('A partir do filme:')
print('\t',src)
print('Foram achados os seguintes filmes recomendados: ')
r = Recommendation.recommend(src, count)
for movie in r :
    print('\t',movie)
Desenha().recomendados(src, r)


print('*'*100)
print('A partir do filme:')
print('\t',src)
print('Com o gênero: ',genero)
print('Foram achados os seguintes filmes recomendados: ')
r2 = Recommendation.recommendInGenre(src, genero, count)
for movie in r2:
    print('\t',movie)
Desenha().recomendados(src, r2)

print('*'*100)

print('A partir do filme:')
print('\t',src)
print('Com a distância: ',distancia)
print('Foi achado o filme: ')
print('\t',Recommendation.recommendCloser(src, distancia))
