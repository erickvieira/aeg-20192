from Grafo_Implementacao import Grafo
from string import ascii_uppercase

class Matriz_Adjacencias:
    def __init__(self, grafo = Grafo()):
        self.TrocarGrafo(grafo)

    def TrocarGrafo(self, grafo = Grafo()):
        self.__grafo = grafo
        self.__matriz = []
        self.__PreencherDefault()

    def __PreencherDefault(self):
        tamanho_grafo = len(self.__grafo.V())
        for i in range(0, tamanho_grafo):
            self.__matriz.append([])
            for j in range(0, tamanho_grafo):
                self.__matriz[i].append(0)

    def CalcularMatriz(self):
        vertices = self.__grafo.V()
        for u in vertices:
            for v in vertices:
                if (self.__grafo.SaoViz(u, v)):
                    i = vertices.index(u)
                    j = vertices.index(v)
                    self.__matriz[i][j] = 1
        return self.__matriz

    def GetMatriz(self):
        return self.__matriz

    def Print(self):
        print(self)

    def __str__(self):
        return (
            'Matriz:\n\n{}'.format(
                self.__matriz
            ).replace(
                '], ', ' \n'
            ).replace(
                '\n[', '\n\t'
            ).replace(
                ']', ''
            ).replace(
                '[', ''
            ).replace(
                ', ', '  '
            ).replace(
                "'", ''
            )
        )