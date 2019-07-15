from turtle import *
from time import sleep
from random import choice

class Desenha:
    def __init__(self):
        self.janela = Screen()
        self.caneta  = Pen()
    def recomendados(self, src, recomendados):
        self.caneta.color('black')
        self.caneta.penup()
        self.caneta.goto(src.coordenada)
        self.caneta.pendown()
        self.caneta.write(src)
        for similar in recomendados:
            print('similar',similar)
            self.caneta.pendown()
            self.caneta.color(choice([
                'red', 'blue', 'green', 'yellow', 'orange', 'gray'
            ]))
            self.caneta.goto(similar.coordenada)
            self.caneta.color('black')
            self.caneta.write(similar)
            self.caneta.penup()
            self.caneta.goto(src.coordenada)
            sleep(0.5)
        self.janela.exitonclick()

    def desenhar(self, movies):
        for item in movies:
            self.caneta.color('black')
            self.caneta.penup()
            self.caneta.goto(item.coordenada)
            self.caneta.pendown()
            self.caneta.write(item)
            self.caneta.color(choice([
                'red', 'blue', 'green', 'yellow', 'orange', 'gray'
            ]))
            for similar in item.similar:
                self.caneta.pendown()
                
                self.caneta.goto(similar.coordenada)
                self.caneta.penup()
                self.caneta.goto(item.coordenada)
                sleep(0.5)
            sleep(0.5)
        self.janela.exitonclick()