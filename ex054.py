import random
comp = random.randint(1, 10)
usuario = 0
tent = 0
while usuario != comp:
    usuario = int(input('Digite um numero 0 a 10: '))
    tent += 1
    if usuario != comp:
        print('Voce errou, o numero nao e {}'.format(usuario))
print('\nVoce acertou, o numero escolhido foi: {}'.format(comp))
print('Voce acertou em {} tentativa(s)'.format(tent))
