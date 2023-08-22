import random
lista = ['pedra', 'papel', 'tesoura']
maquina = random.choice(lista)
usuario = str(input('Escolha entre Pedra, Papel ou Tesoura\nSua escolha: '))
if maquina == 'pedra' and usuario == 'tesoura':
    print('a maquina ganhou')
elif maquina == 'papel' and usuario == 'pedra':
    print('a maquina ganhou')
elif maquina == 'tesoura' and usuario == 'papel':
    print('a maquina ganhou')
elif maquina == 'pedra' and usuario == 'papel':
    print('voce ganhou')
elif maquina == 'papel' and usuario == 'tesoura':
    print('voce ganhou')
elif maquina == 'tesoura' and usuario == 'pedra':
    print('voce ganhou')
else:
    print('empatou')
print('a maquina escolheu: {}'.format(maquina))