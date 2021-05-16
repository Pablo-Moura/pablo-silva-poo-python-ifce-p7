"""

O triângulo pode ser classificado com base no comprimento de
seus lados em equilátero, isósceles ou escaleno. Todos os três lados de um
triângulo equilátero têm o mesmo comprimento. Um triângulo isósceles tem dois
lados que são do mesmo comprimento e um terceiro lado que é diferente comprimento.
Se todos os lados tiverem comprimentos diferentes, o triângulo é escaleno.
Escreva um programa que leia os comprimentos dos três lados de um triângulo do usuário. Em seguida, exiba uma mensagem que declara o tipo do triângulo.

"""

from ladosDoTriangulo import *

def descobrirLados():
    if ladoA == ladoB and ladoA == ladoC:
        print('O Triângulo tem TODOS os lados IGUAIS, então é um Triângulo Equilátero')
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print('O Triângulo tem DOIS lados IGUAIS, então é um Triângulo Isósceles')
    else:
        print('O Triângulo tem TODOS os lados DIFERENTES, então é um Triângulo Escaleno')

descobrirLados()