import os
from os import system, startfile
import graphviz

class Grafica:
    def __init__(self, matriz, frecuencia):
        self.matriz = matriz
        self.frecuencia = frecuencia
        self.create_graph()

    def create_graph(self):
        img_route = "Matriz de frecuencia" + str(self.frecuencia)