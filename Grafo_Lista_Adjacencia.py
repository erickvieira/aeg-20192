from Grafo_Interface import IGrafo
from string import ascii_uppercase
import re

class Grafo(IGrafo):

    def __init__(self, orientado = False):
        self._vertices = {}
        self._orientado = orientado
        self._vazio = False

    def _ChecarListaVazia(self):
        self._vazio = True
        self._vazio = self._vazio and self._vertices == []
        if not self._vazio:
            for no in self._vertices:
                self._vazio = self._vazio and no == []
        return self._vazio

    def DefinirN(self, n = 1):
        self._vertices = {}
        self.n = n
        for i in range(0, self.n):
            self._vertices[ascii_uppercase[i]] = []
        return self._vertices

    def V(self):
        vertices = []
        for no in self._vertices:
            vertices.append(no)
        return vertices

    def _PercorrerGrafo(self, callback = None):
        for no in self._vertices:
            for viz in self._vertices[no]:
                if callback:
                    callback(no, viz)

    def E(self):
        arestas = []
        if self._ChecarListaVazia():
            return arestas
        def criar_aresta(no, viz):
            if (not self._orientado):
                arestas.append((no, viz))
            else:
                if (viz, no) not in arestas:
                    arestas.append((no, viz))
        self._PercorrerGrafo(criar_aresta)
        arestas.sort()
        return arestas

    def RemoverAresta(self, u = '', v = ''):
        if v == '' or u == '':
            return None
        else:
            u = u.upper()
            v = v.upper()
        if self._ChecarListaVazia():
            raise Exception('ERRO: grafo vazio. Por favor, use o medoto ".DefinirN()" para inicializar a estrutura.')
        if (u not in self._vertices) or (v not in self._vertices):
            raise Exception('ERRO: a aresta (%s, %s) nao foi encontrada.' % (u, v))
        else:
            self._vertices[u].remove(v)
            if (not self._orientado):
                self._vertices[v].remove(u)
                return [(u, v), (v, u)]
        return [(u, v)]

    def AdicionarAresta(self, u = '', v = ''):
        if v == '' or u == '':
            return self._vertices
        if v == u:
            return self._vertices
        else:
            u = u.upper()
            v = v.upper()
        if self.SaoViz(u, v):
            return self._vertices
        if self._ChecarListaVazia():
            raise Exception('ERRO: grafo vazio. Por favor, use o medoto ".DefinirN()" para inicializar a estrutura.')
        self._vertices[u].append(v)
        if (not self._orientado):
            self._vertices[v].append(u)
        return self._vertices

    def SaoViz(self, u = '', v = ''):
        return u in self._vertices[v]

    def Viz(self, v, Tipo="*", Fechada=False):
        vizinhos_de_v = self._vertices[v]
        if (Fechada):
            vizinhos_de_v.append(v)
        return vizinhos_de_v
    
    def Print(self):
        print(self)

    def __str__(self):
        if self._ChecarListaVazia():
            return 'Grafo vazio'
        else:
            regex = re.compile(r"([\]][,][\s])")
            return (
                regex.sub(
                    "]\n\t", 
                    "Grafo G:\n {}".format(self._vertices)
                ).replace(
                    '{', '\n\t'
                ).replace(
                    '}', "\n"
                ).replace(
                    ': ', ' é vizinho de '
                ).replace(
                    '[]', 'NINGUÉM'
                ).replace(
                    '[', ''
                ).replace(
                    ']', ''
                ).replace(
                    "'", '' 
                )
            )
