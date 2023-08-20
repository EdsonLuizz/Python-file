s = float(input('Qual é o seu salario? '))
if s > 1250:
    aumento = s * 0.10
    salario = aumento + s
    print('salario ajustado: R${:.2f}'.format(salario))
else:
    aumento = s * 0.15
    salario = aumento + s
    print('salario ajustado: R${:.2f}'.format(salario))