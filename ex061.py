cont = 1
maior = 0
menor = 0
r = 's'
soma = 0
while r == 's':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar[S/N]: ')).lower()
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if r == 's':
        cont += 1
    soma = soma + n
media = soma / cont
print('Voce digitou {} numeros e a media foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


