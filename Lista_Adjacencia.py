from Grafo_Implementacao import Grafo

class Lista_Adjacencia:
    def __init__(self, grafo = Grafo()):
        self.TrocarGrafo(grafo)

    def TrocarGrafo(self, grafo = Grafo()):
        self.__grafo = grafo

    def GetLista(self, v):
        return self.__grafo.Viz(v)