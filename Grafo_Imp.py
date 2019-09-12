from Grafo_Interface import Grafo
from Vertice import Vertice

class GrafoImp(metaclass=Grafo):

    def __init__(self, direct = True):
        super.__init__()
        self.vertices = []
        self.arestas = []

    def DefinirN(self, n):
        self.n = n
        return

    def V(self):
        return