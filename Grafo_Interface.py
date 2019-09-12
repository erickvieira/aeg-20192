import abc


class Grafo(metaclass=abc.ABCMeta):
    # Classe base abstrata para representações de grafos

    def __init__(self, direct=True):
            # Grafo se direct=False ou Digrafo se direct=True.
        self.n, self.m, self.orientado = None, None, orientado

    @abc.abstractmethod
    def DefinirN(self, n):
        # Define o número n de vértices.
        pass

    @abc.abstractmethod
    def V(self):
            # Retorna a lista de vértices.
        pass

    @abc.abstractmethod
    def E(self):
        # Retorna lista de arestas uv.
        pass

    @abc.abstractmethod
    def RemoverAresta(self, u, v):
        # Remove a aresta uv.
        pass

    @abc.abstractmethod
    def AdicionarAresta(self, u, v):
        # Adiciona aresta uv.
        pass

    @abc.abstractmethod
    def SaoViz(self, u, v):
        # Retorna True se e somente se uv é uma aresta.
        pass

    @abc.abstractmethod
    def Viz(self, v, Tipo="*", Fechada=False):
        """
        Retorna lista de vértices vizinhos do vértice v. Se Fechada=True, o próprio v é incluido na lista.
        Tipo="*" significa listar todas as arestas incidentes em v. Se G é orientado, 
        Tipo="+" (resp. "-") significa listar apenas as arestas de saída (resp. entrada) de v.
        """
        pass
