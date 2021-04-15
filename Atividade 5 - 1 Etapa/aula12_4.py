"""

Se você tiver 3 canudos, possivelmente de comprimentos diferentes, pode ou não ser possível colocá-los de forma que formem um triângulo quando suas pontas se tocam. Por exemplo, se todos os canudos têm um comprimento de 6 cm , então pode-se facilmente construir um triângulo equilátero usando-os. No entanto, se um canudo tiver 15 centímetros de comprimento, enquanto os outros dois têm apenas 5 centímetros de comprimento, então um triângulo não pode ser formado. Mais geralmente, se qualquer comprimento for maior ou igual à soma dos outros dois, os comprimentos não podem ser usados ​​para formar um triângulo. Caso contrário, eles podem formar um triângulo.
Escreva uma função que determine se três comprimentos podem ou não formar um triângulo. A função terá 3 parâmetros e retornará um resultado booleano. Se qualquer um dos comprimentos for menor ou igual a 0, sua função deve retornar False. Caso contrário, deve determinar se os comprimentos podem ou não ser usados ​​para formar um triângulo usando o método descrito no parágrafo anterior e retornar o resultado apropriado.
Além disso, escreva um programa que leia 3 valores inteiros de tamanhos informados do usuário e demonstre o comportamento de sua função.

se qualquer comprimento for maior ou igual à soma dos outros dois, os comprimentos não podem ser usados
para formar um triângulo. Caso contrário, eles podem formar um triângulo.

A função terá 3 parâmetros e retornará um resultado booleano. Se qualquer um dos comprimentos for menor
ou igual a 0, sua função deve retornar False.
"""

class Triangulos:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def formarTriangulo(self):
        if self.ladoA <= 0 or self.ladoB <= 0 or self.ladoC <= 0:
            return False

        soma1 = self.ladoA + self.ladoB
        soma2 = self.ladoA + self.ladoC
        soma3 = self.ladoB + self.ladoC

        if self.ladoA >= soma3 or self.ladoB >= soma2 or self.ladoC >= soma1:
            return f'Não é possível formar um triângulo com os lados atribuídos.'
        else:
            return f'Um triângulo pode ser formado com os lados atribuídos'


triangulo1 = Triangulos(int(input('Digite o 1º lado do Triangulo - (em cm): ')), int(input('Digite o 2º lado do Triangulo - (em cm): ')), int(input('Digite o 3º lado do Triangulo - (em cm): ')))
print(triangulo1.formarTriangulo())