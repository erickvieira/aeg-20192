from Grafo_Interface import IGrafo
from random import randint
from string import ascii_uppercase

class Grafo(IGrafo):

    def __init__(self, direct = True):
        self.nos = {}

    def __ChecarListaVazia(self):
        vazio = True
        for no in self.nos:
            vazio = vazio and no == []
        return vazio

    def DefinirN(self, n = 1):
        self.nos = {}
        for i in range(0, n):
            self.nos[ascii_uppercase[i]] = []
        return self.nos

    def V(self):
        vertices = []
        for no in self.nos:
            vertices.append(no)
        return vertices

    def E(self):
        arestas = []
        if self.__ChecarListaVazia():
            return arestas
        for no in self.nos:
            for viz in self.nos[no]:
                if (viz, no) not in arestas:
                    arestas.append((no, viz))
        return arestas

    def RemoverAresta(self, u = '', v = ''):
        if v == '' or u == '':
            return None
        else:
            u = u.upper()
            v = v.upper()
        if self.__ChecarListaVazia():
            raise Exception('ERRO: grafo vazio. Por favor, use o medoto ".DefinirN()" para inicializar a estrutura.')
        if (u not in self.nos) or (v not in self.nos):
            raise Exception('ERRO: a aresta (%s, %s) nao foi encontrada.' % (u, v))
        else:
            self.nos[u].remove(v)
            self.nos[v].remove(u)
        return [(u, v), (v, u)]

    def AdicionarAresta(self, u = '', v = ''):
        if v == '' or u == '':
            return self.nos
        if v == u:
            return self.nos
        else:
            u = u.upper()
            v = v.upper()
        if self.SaoViz(u, v):
            return self.nos
        if self.__ChecarListaVazia():
            raise Exception('ERRO: grafo vazio. Por favor, use o medoto ".DefinirN()" para inicializar a estrutura.')
        self.nos[u].append(v)
        self.nos[v].append(u)
        return self.nos

    def SaoViz(self, u = '', v = ''):
        return u in self.nos[v] and v in self.nos[u]

    def Viz(self, v, Tipo="*", Fechada=False):
        return self.nos[v]

    def __str__(self):
        return self.nos
