from Grafo_Implementacao import Grafo
from random import randint
import Utils as utils

grafo = Grafo()
limite = randint(1, 20)
print('> GERANDO GRAFO DE %02d VERTICES' % limite)
grafo.DefinirN(limite)

print('= ADICIONANDO ARESTAS =================')
grafo = utils.gerarGrafo(limite, grafo)
print(grafo.nos)
print('=======================================\n')

print('= CONJUNTOS ===========================')
print('- DE VERTICES: %s' % grafo.V())
print('- DE ARESTAS:  %s' % grafo.E())
print('=======================================\n')
