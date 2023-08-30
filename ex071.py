n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))
lista = (n1, n2, n3, n4)
print('=-' * 15)
print(f'O numero 9 apareceu {lista.count(9)} vez(es)')
if 3 in lista:
    print(f'O numero 3 apareceu primeiro na posicao {lista.index(3) + 1}')
else:
    print('O numero 3 nao foi digitado em nenhuma posicao')
print('=-' * 15)
print('OS NUMEROS PARES SÃO:')
for c in lista:
    if c % 2 == 0:
        print(c, end=' ')
