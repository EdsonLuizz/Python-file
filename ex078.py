lista = []
pares = []
impares = []
resp = 's'
while resp != 'n':
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        pares.append(n)
    if n % 2 != 0:
        impares.append(n)
    lista.append(n)
    resp = str(input('Quer continuar?[S/N] ')).lower()
    while resp != 's' and resp != 'n':
        resp = str(input('Quer continuar?[S/N] ')).lower()
print('=-' * 12)
lista.sort()
print(f'Numeros digitados: {lista}')
print(f'Conjunto dos numeros pares: {pares}')
print(f'Conjunto dos numeros impares: {impares}')