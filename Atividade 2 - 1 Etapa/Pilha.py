# Começar criando uma lista vazia para repreendido a pilha
pilha = []
print(f'\nTemos um total de {len(pilha)} roupas na pilha.\n')

# Aqui será adicionado algumas roupas na nossa pilha
for x in range(1, 16):
    print(f'Roupa de número {x} chegando na pilha')
    pilha.insert(0, x)

# Mostrando nossa pilha de roupas
print(f'\nNo momento temos {len(pilha)} roupas na pilha.')
print(f'{pilha}\n')

# Dobrando e tirando algumas roupas da nossa pilha
for x in range(15, 8, -1):
    print(f'Roupa de número {x} foi dobrada')
    pilha.pop(0)

# Mostrando a pilha atual
print(f'\nTemos agora {len(pilha)} roupas na pilha.')
print(f'{pilha}\n')
print(f'Trade de dobrar elas depois!\n')

# Fim da demonstração
