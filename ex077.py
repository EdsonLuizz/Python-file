lista = []
cont = 0
resp = 's'
while resp != 'n':
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    resp = str(input('Quer continuar?[S/N] ')).lower()
    while resp != 's' and resp != 'n':
        resp = str(input('Quer continuar?[S/N] ')).lower()
print('=-' * 11)
lista.sort(reverse=True)
print(f'Foram digitados {cont} numeros')
print(f'Lista ordenada: {lista}')
if 5 in lista:
    print('O numero 5 foi digitado e esta na lista')
else:
    print('O numero 5 NAO foi digitado')