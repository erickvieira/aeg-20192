from string import ascii_uppercase
from random import randint

def gerarGrafo(limite, grafo):
    letras = [ch for ch in ascii_uppercase]
    for u in range(limite - 1):
        for E in range(randint(0, limite - 1)):
            grafo.AdicionarAresta(letras[u], letras[randint(0, limite - 1)])
    return grafo
