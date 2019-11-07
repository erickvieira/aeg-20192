from Grafo_Interface import IGrafo
from string import ascii_uppercase

class Grafo(IGrafo):
    def __init__(self, orientado = False):
        self.__matriz = []
        self.__orientado = orientado
        self.__vazio = True

    def DefinirN(self, n):
        self.n = n
        for i in range(0, self.n):
            self.__matriz.append([0 for j in range(0, self.n)])
        return self.__matriz

    def V(self):
        return [i for i in range(0, self.n)]

    def E(self):
        arestas = []
        u = None
        v = None
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.__matriz[i][j] != 0:
                    u = ascii_uppercase[i]
                    v = ascii_uppercase[j]
                    if not self.__orientado:
                        arestas.append((u, v))
                    else:
                        if (u, v) not in arestas:
                            arestas.append((u, v))
        arestas.sort()
        return arestas

    def RemoverAresta(self, u = '', v = ''):
        i = ascii_uppercase.index(u)
        j = ascii_uppercase.index(v)
        self.__matriz[i][j] = 0
        if not self.__orientado:
            self.__matriz[j][i] = 0
            return [(u, v), (v, u)]
        return [(u, v)]

    def AdicionarAresta(self, u = '', v = ''):
        self.__vazio = False
        i = ascii_uppercase.index(u)
        j = ascii_uppercase.index(v)
        self.__matriz[i][j] = 1
        if not self.__orientado:
            self.__matriz[j][i] = 1
        return self.__matriz

    def SaoViz(self, u = '', v = ''):
        i = ascii_uppercase.index(u)
        j = ascii_uppercase.index(v)
        if not self.__orientado:
            return self.__matriz[i][j] == 1 and self.__matriz[i][j] == 1
        else:
            return self.__matriz[i][j] == 1

    def Viz(self, v, Tipo="*", Fechada=False):
        i = ascii_uppercase.index(v)
        vizinhos_de_v = []
        for j in range(0, self.n):
            if self.__matriz[i][j] == 1:
                vizinhos_de_v.append(ascii_uppercase[j])
        if Fechada:
            vizinhos_de_v.append(v)
        return vizinhos_de_v

    def __str__(self):
        if self.__vazio:
            return 'Grafo vazio'
        else:
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