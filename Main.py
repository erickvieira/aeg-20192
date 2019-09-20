from Grafo_Implementacao import Grafo
from Matriz_Adjacencias import Matriz_Adjacencias
from random import randint
import Utils as utils

grafo = Grafo()
limite = randint(1, 26)
print('> GERANDO GRAFO DE %02d VERTICES\n\n' % limite)
grafo.DefinirN(limite)

print('= ADICIONANDO ARESTAS =================')
grafo = utils.gerarGrafo(limite, grafo)
print(grafo)
print('=======================================\n')

print('= CONJUNTOS ===========================')
print('- DE VERTICES: %s' % grafo.V())
print('- DE ARESTAS:  %s' % grafo.E())
print('=======================================\n')

matriz = Matriz_Adjacencias(grafo)
matriz.CalcularMatriz()

print('= MATRIZ DE ADJACENCIAS ===============')
print(matriz)
print('=======================================\n')
