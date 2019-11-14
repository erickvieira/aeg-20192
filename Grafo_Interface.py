from abc import ABCMeta, abstractmethod

class IGrafo(metaclass=ABCMeta):
    # Classe base abstrata para representações de grafos

    @abstractmethod
    def __init__(self, orientado = False):
            # Grafo se direct=False ou Digrafo se direct=True.
        self.n, self.m, self._orientado = orientado

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
    
    def __vizinhos_nao_marcados_de_v(self, marcados = {}, v = ""):
        return filter(lambda x: not marcados[x], self.Viz(v))
    
    def BuscaLargura(self, visitarNo = lambda u, v: print((u, v))):
        vertices = self.V()
        marcados = { key: False for key in vertices }
        marcados[vertices[0]] = True
        F = []
        F.append(vertices[0])
        while F:
            for w in filter(lambda x: not marcados[x], self.Viz(F[0])):
                if not marcados[w]:
                    visitarNo(F[0], w)
                    marcados[w] = True
                    F.append(w)
                else:
                    if w in F:
                        visitarNo(F[0], w)
            marcados[F.pop(0)] = True
    
    def BuscaProfundidade(self, visitarNo = lambda u, v: print((u, v))):
        vertices = self.V()
        marcados = { key: False for key in vertices }
        P = []
        def p(v):
            marcados[v] = True
            P.insert(0, v)
            for w in filter(lambda x: not marcados[x], self.Viz(v)):
                if not marcados[w]:
                    visitarNo(P[0], w)
                    p(w)
                else:
                    if w in P:
                        visitarNo(P[0], w)
            marcados[P.pop(0)] = True
        p(vertices[0])
    
    def BuscaCompleta(self, visitarNo = lambda u, v: print((u, v))):
        if not self._orientado:
            raise Exception('FATAL: impossível rodar uma BuscaCompleta em um grafo que não seja DÍGRAFO.')
        else :
            vertices = self.V()
            marcados = { key: False for key in vertices }
            P = []
            def p(v):
                marcados[v] = True
                P.insert(0, v)
                for w in filter(lambda x: not marcados[x], self.Viz(v)):
                    visitarNo(P[0], w)
                    if not marcados[w]:
                        p(w)
                marcados[P.pop(0)] = True
            for r in vertices:
                if not marcados[r]:
                    p(r)
    
    def ComponentesFortementeConexas(self, visitarNo = lambda u, v: print((u, v))):
        if not self._orientado:
            raise Exception('FATAL: impossível rodar procurar ComponentesFortementeConexas em um grafo que não seja DÍGRAFO.')
        else:
            pass
    
    def BuscaIrProf(self, visitarNo = lambda u, v: print((u, v))):
        vertices = self.V()
        marcados = { key: False for key in vertices }
        P = []
        def p(v):
            marcados[v] = True
            P.insert(0, v)
            for w in filter(lambda x: not marcados[x], self.Viz(v)):
                if w not in P:
                    visitarNo(v, w)
                    p(w)
            marcados[P.pop(0)] = False
        p(vertices[0])
    
    def BuscarCiclosSimples(
        self, 
        visitarNo = lambda u, v: print((u, v)),
        capturarCiclos = lambda ciclos: print(ciclos)
    ):
        vertices = self.V()
        marcados = { key: False for key in vertices }
        ciclos = { key: [] for key in vertices }
        P = []
        def p(v):
            marcados[v] = True
            P.insert(0, v)
            for w in self.Viz(v):
                if w not in P:
                    visitarNo(v, w)
                    p(w)
                if w not in ciclos[v]:
                    ciclos[v].append(w)
            marcados[P.pop(0)] = False
        p(vertices[0])
        for ciclo in ciclos:
            if len(ciclos[ciclo]) > 2:
                capturarCiclos(ciclos[ciclo])
