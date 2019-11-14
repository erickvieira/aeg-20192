#!/bin/python3
from Grafo_Lista_Adjacencia import Grafo

print('Busca irrestrita - Grafo 4 posições')

grafo = Grafo()
grafo.DefinirN(4)
grafo.AdicionarAresta('A', 'B')
grafo.AdicionarAresta('A', 'D')
grafo.AdicionarAresta('C', 'B')
grafo.AdicionarAresta('C', 'A')

print('Arestas: {}'.format(grafo.E()))

print('\nRodando a busca')
grafo.BuscarCiclosSimples()
