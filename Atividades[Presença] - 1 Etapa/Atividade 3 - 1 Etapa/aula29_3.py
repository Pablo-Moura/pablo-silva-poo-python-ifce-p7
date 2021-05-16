"""
Para ganhar o prêmio máximo na Mega Sena, é necessário
acertar todos os 6 números em seu bilhete com os 6 números entre 1 e 60
sorteados. Escreva um programa que gere uma seleção aleatória de 6 números para
uma aposta. Certifique-se de que os 6 números selecionados não contenham
duplicatas. Exibir os números em ordem crescente.

"""

import random

def repetido():
    if len(sorteadoLista) != len(set(sorteadoLista)):
        sorteadoLista2 = set(sorteadoLista)

sorteadoLista = []
sorteadoLista2 = []

while len(sorteadoLista2) < 6:
    sorteado = random.randrange(1,61)
    sorteadoLista.append(sorteado)
    repetido()
    sorteadoLista2 = set(sorteadoLista)

print(sorted(sorteadoLista2))