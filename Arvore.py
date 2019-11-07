from Grafo_Lista_Adjacencia import Grafo_Lista_Adjacencia
from random import randint
from string import ascii_uppercase

class Arvore_Lista_Adjacencia(Grafo_Lista_Adjacencia):
    
    def __init__(self, orientado = False):
        super().__init__(self)
        self._orientado = orientado
    
    def __PodarNo(self, no = '', nos = []):
        vizinhos = self.Viz(no)
        for vizinho in vizinhos:
            self.RemoverAresta(no, vizinho)
        nos.remove(no)
        return vizinhos
    
    def CentroArv(self):
        nos = list(self._vertices)
        while not (len(nos) == 1 and (self.n % 2) == 1) or (len(nos) == 2 and (self.n % 2) == 0):
            for no in nos:
                if len(self._vertices[no]) == 1 and no != 'A':
                    self.__PodarNo(no, nos)
        return nos
