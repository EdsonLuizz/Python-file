n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero (999 para parar): '))
    if n != 999:
        cont += 1
        soma = soma + n
print(f'Foram digitados {cont} valores')
print(f'A soma dos numeros digitados: {soma}')
