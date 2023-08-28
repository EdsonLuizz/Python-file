import random
v = 0
while True:
    comp = random.randint(0, 10)
    usuario = int(input('Diga um valor: '))
    total = comp + usuario
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]? ')).upper().strip()[0]
    print(f'Voce jogou {usuario} e o computador jogou {comp}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce ganhou')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce ganhou')
            v += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER!!!! Voce vencer {v} vezes')

