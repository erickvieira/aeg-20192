from Grafo_Implementacao import Grafo
from string import ascii_uppercase
from random import randint
from Utils import split_str

grafo = Grafo()
limite = randint(1, 20)
letras = split_str(ascii_uppercase)
print('> GERANDO GRAFO DE %d VERTICES' % limite)
grafo.DefinirN(limite)

print('= ADICIONANDO ARESTAS =================')
def gerarArestasAleatoriamente(limite, grafo):
	for u in range(limite - 1):
		for E in range(randint(0, limite - 1)):
			grafo.AdicionarAresta(letras[u], letras[randint(0, limite - 1)])
	return grafo
grafo = gerarArestasAleatoriamente(limite, grafo)
print(grafo.nos)
print('=======================================\n')

print('= CONJUNTOS ===========================')
print('- DE VERTICES: %s' % grafo.V())
print('- DE ARESTAS:  %s' % grafo.E())
print('=======================================\n')
