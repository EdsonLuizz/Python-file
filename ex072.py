listagem = ('Lapis', 1.75, 'Caderno', 12.9, 'Transferidor', 8.90, 'Caneta', 1.00, 'Borracha', 1.50)
print('-' * 30)
print(f'{"LISTAGEM DE PRECOS":^30}')
print('-' * 30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<21}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('=' * 30)