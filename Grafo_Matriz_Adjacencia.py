from Grafo_Interface import IGrafo
from string import ascii_uppercase

class Grafo_Matriz_Adjacencia(IGrafo):
    def __init__(self, orientado = False):
        self.__matriz = []
        self.__orientado = orientado

    def DefinirN(self, n):
        self.n = n
        for i in n:
            self.__matriz.append([])
            for j in n:
                self.__matriz[i].append(0)
        pass

    def V(self):
        return [i for i in range(1, self.n)]

    def E(self):
        arestas = []
        u = None
        v = None
        for i in n:
            for j in n:
                if self.__matriz[i][j] != 0:
                    u = ascii_uppercase[i]
                    v = ascii_uppercase[j]
                    if not self.orientado:
                        arestas.append((u, v))
                    else:
                        if (u, v) not in arestas:
                            arestas.append((u, v))
        arestas.sort()
        return arestas

    def RemoverAresta(self, u, v):
        i = ascii_uppercase.index(u)
        j = ascii_uppercase.index(v)
        self.__matriz[i][j] = 0
        if not self.__orientado:
            self.__matriz[i][j] = 0
        pass

    def AdicionarAresta(self, u, v):
        # Adiciona aresta uv.
        pass

    def SaoViz(self, u, v):
        # Retorna True se e somente se uv é uma aresta.
        pass

    def Viz(self, v, Tipo="*", Fechada=False):
        """
        Retorna lista de vértices vizinhos do vértice v. Se Fechada=True, o próprio v é incluido na lista.
        Tipo="*" significa listar todas as arestas incidentes em v. Se G é orientado, 
        Tipo="+" (resp. "-") significa listar apenas as arestas de saída (resp. entrada) de v.
        """
        pass