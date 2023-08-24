s = 0
n = 0
for c in range(0, 7):
    nasc = int(input('Digite a sua data de nascimento: '))
    maioridade = 2023 - nasc
    if maioridade >= 21:
        s += 1
    else:
        n += 1
print('{} pessoa(s) ja atingiram a maioridade\n{} pessoa(s) ainda nao atingiram a maioridade'.format(s, n))