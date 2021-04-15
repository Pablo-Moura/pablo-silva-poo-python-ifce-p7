# Começo criando uma lista vazia que irá representar a fila.
fila = []
print(f'\nO caixa esta fechado com {len(fila)} pessoas na fila.\n')

# Adicionando pessoas à fila do caixa.
for x in range (1, 7):
    print(f'Chegou a {x}a pessoa na fila do caixa.')
    fila.append(x)
    
# Mostrando o numero de pessoas presentes na fila
print(f'\nTemos {len(fila)} pessoas na fila do caixa.')
print(f'{fila}\n')

# O caixa abriu, mostrando quantas pessoas passaram nele
print(f'O caixa abriu, pessoas estao passando por ele.\n')
for x in range (1, 5):
    print(f'A {x}a pessoa passou no caixa.')
    fila.pop(0)

# Mostrando a fila atual
print(f'\nTemos agora {len(fila)} pessoas na fila do caixa.')
print(f'{fila}\n')

# Movendo a fila
for x in range (5, 7):
    y = x - 4
    print(f'A {x}a pessoa passou para frente e esta em {y}o na fila')
    fila.append(y)
    
# Atualizando a fila
for x in range (1, 3):
    fila.pop(0)

# Mostrando a fila atual
print(f'\nFila atual do caixa:')
print(f'{fila}')

# Fim da Demonstração da Fila
