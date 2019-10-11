from Grafo_Lista_Adjacencia import Grafo_Lista_Adjacencia
from Grafo_Matriz_Adjacencia import Grafo_Matriz_Adjacencia
from Arvore import Arvore_Lista_Adjacencia
from random import randint
import Utils as utils

def main():
    arvore = Arvore_Lista_Adjacencia(orientado=False)
    arvore.DefinirN(7)
    
    arvore.AdicionarAresta('A', 'B')
    arvore.AdicionarAresta('A', 'C')
    arvore.AdicionarAresta('B', 'D')
    arvore.AdicionarAresta('B', 'E')
    arvore.AdicionarAresta('C', 'F')
    arvore.AdicionarAresta('C', 'G')
    
    print(arvore)

    print("Centro de G: {}".format(arvore.CentroArv()))

    # grafo = Grafo_Lista_Adjacencia()
    # limite = randint(1, 26)
    # print('> GERANDO GRAFO DE %02d VERTICES\n\n' % limite)
    # grafo.DefinirN(limite)

    # print('= ADICIONANDO ARESTAS =================')
    # grafo = utils.gerarGrafo(limite, grafo)
    # print(grafo)
    # print('=======================================\n')

    # print('= CONJUNTOS ===========================')
    # print('- DE VERTICES: %s' % grafo.V())
    # print('- DE ARESTAS:  %s' % grafo.E())
    # print('=======================================\n')

    # matriz = Grafo_Matriz_Adjacencia(grafo)

    # print('= MATRIZ DE ADJACENCIAS ===============')
    # print(matriz)
# print('=======================================\n')

if __name__ == '__main__':
    main()