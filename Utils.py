from string import ascii_uppercase
from random import randint

def split_str(s):
    return [ch for ch in s]

def gerarGrafo(limite, grafo):
    letras = split_str(ascii_uppercase)
    for u in range(limite - 1):
        for E in range(randint(0, limite - 1)):
            grafo.AdicionarAresta(letras[u], letras[randint(0, limite - 1)])
    return grafo
