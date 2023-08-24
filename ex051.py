maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Qual e o peso da {} pessoa? '.format(c + 1)))
    if c == 0:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi de {}Kg\no menor peso lido foi de {}Kg'.format(maior, menor))