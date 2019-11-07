from abc import ABCMeta, abstractmethod

class IGrafo(metaclass=ABCMeta):
    # Classe base abstrata para representações de grafos

    @abstractmethod
    def __init__(self, orientado=False):
            # Grafo se direct=False ou Digrafo se direct=True.
        self.n, self.m, self.orientado = orientado

    @abstractmethod
    def DefinirN(self, n):
        # Define o número n de vértices.
        pass

    @abstractmethod
    def V(self):
            # Retorna a lista de vértices.
        pass

    @abstractmethod
    def E(self):
        # Retorna lista de arestas uv.
        pass

    @abstractmethod
    def RemoverAresta(self, u, v):
        # Remove a aresta uv.
        pass

    @abstractmethod
    def AdicionarAresta(self, u, v):
        # Adiciona aresta uv.
        pass

    @abstractmethod
    def SaoViz(self, u, v):
        # Retorna True se e somente se uv é uma aresta.
        pass

    @abstractmethod
    def Viz(self, v, Tipo="*", Fechada=False):
        """
        Retorna lista de vértices vizinhos do vértice v. Se Fechada=True, o próprio v é incluido na lista.
        Tipo="*" significa listar todas as arestas incidentes em v. Se G é orientado, 
        Tipo="+" (resp. "-") significa listar apenas as arestas de saída (resp. entrada) de v.
        """
        pass
    
    def BuscaLargura(self, callback = lambda u, v: print((u, v))):
        marcados = { key: False for key in self.V() }
        marcados[self.V()[0]] = True
        F = []
        F.append(self.V()[0])
        while F:
            vizinhos_de_v = filter(lambda x: not marcados[x], self.Viz(F[0]))
            for w in vizinhos_de_v:
                if not marcados[w]:
                    callback(F[0], w)
                    marcados[w] = True
                    F.append(w)
                else:
                    if w in F:
                        callback(F[0], w)
            marcados[F.pop(0)] = True
