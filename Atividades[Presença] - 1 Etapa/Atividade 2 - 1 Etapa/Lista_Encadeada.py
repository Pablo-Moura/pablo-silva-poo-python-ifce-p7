# Import necessário para a função random
import random

# Criando nossa lista de aulas que representará a lista encadeada
lista = ['poo', 'sor', 'hst', 'emp']

# Adicionando mais aulas na nossa lista
lista.insert(0, 'engs')
lista.insert(1, 'bd')
lista.insert(0, 'edf')
listaEnc = sorted(lista)

# Mostrando a lista de aulas
print(f'\nTenho {len(listaEnc)} aulas nessa semana.')
print(f'{listaEnc}\n')

# Assistindo algumas aulas da semana
aula = list(range(1, 4))
random.shuffle(aula)
for x in aula:
    print(f'A aula de {listaEnc[x]} foi assistida.')
    listaEnc.pop(x)

# Mostrando as aulas atuais
print(f'\nAgora restam {len(listaEnc)} aulas nessa semana.')
print(f'{listaEnc}')

# Fim da Demonstração da Lista Encadeada
