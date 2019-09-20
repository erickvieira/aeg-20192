from Grafo_Interface import IGrafo
from random import randint
from string import ascii_uppercase
import re

class Grafo(IGrafo):

    def __init__(self, orientado = False):
        self.__vertices = {}
        self.__orientado = orientado
        self.__vazio = False

    def __ChecarListaVazia(self):
        self.__vazio = True
        self.__vazio = self.__vazio and self.__vertices == []
        if not self.__vazio:
            for no in self.__vertices:
                self.__vazio = self.__vazio and no == []
        return self.__vazio

    def DefinirN(self, n = 1):
        self.__vertices = {}
        for i in range(0, n):
            self.__vertices[ascii_uppercase[i]] = []
        return self.__vertices

    def V(self):
        vertices = []
        for no in self.__vertices:
            vertices.append(no)
        return vertices

    def __PercorrerGrafo(self, callback = None):
        for no in self.__vertices:
            for viz in self.__vertices[no]:
                if callback:
                    callback(no, viz)

    def E(self):
        arestas = []
        if self.__ChecarListaVazia():
            return arestas
        def criar_aresta(no, viz):
            if (not self.__orientado):
                arestas.append((no, viz))
            else:
                if (viz, no) not in arestas:
                    arestas.append((no, viz))
        self.__PercorrerGrafo(criar_aresta)
        arestas.sort()
        return arestas

    def RemoverAresta(self, u = '', v = ''):
        if v == '' or u == '':
            return None
        else:
            u = u.upper()
            v = v.upper()
        if self.__ChecarListaVazia():
            raise Exception('ERRO: grafo vazio. Por favor, use o medoto ".DefinirN()" para inicializar a estrutura.')
        if (u not in self.__vertices) or (v not in self.__vertices):
            raise Exception('ERRO: a aresta (%s, %s) nao foi encontrada.' % (u, v))
        else:
            self.__vertices[u].remove(v)
            if (not self.__orientado):
                self.__vertices[v].remove(u)
        return [(u, v), (v, u)]

    def AdicionarAresta(self, u = '', v = ''):
        if v == '' or u == '':
            return self.__vertices
        if v == u:
            return self.__vertices
        else:
            u = u.upper()
            v = v.upper()
        if self.SaoViz(u, v):
            return self.__vertices
        if self.__ChecarListaVazia():
            raise Exception('ERRO: grafo vazio. Por favor, use o medoto ".DefinirN()" para inicializar a estrutura.')
        self.__vertices[u].append(v)
        if (not self.__orientado):
            self.__vertices[v].append(u)
        return self.__vertices

    def SaoViz(self, u = '', v = ''):
        return u in self.__vertices[v] and v in self.__vertices[u]

    def Viz(self, v, Tipo="*", Fechada=False):
        vizinhos_de_v = self.__vertices[v]
        if (Fechada):
            vizinhos_de_v.append(v)
        return vizinhos_de_v
    
    def Print(self):
        print(self)

    def __str__(self):
        if self.__ChecarListaVazia():
            return 'Grafo vazio'
        else:
            regex = re.compile(r"([\]][,][\s])")
            return (
                regex.sub(
                    "]\n\t", 
                    "Grafo G:\n {}".format(self.__vertices)
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
