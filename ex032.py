valor = float(input('Qual e o valor da casa? '))
salario = float(input('Qual e o valor do salario do comprador? '))
anos = int(input('Em quantos anos voce pretende pagar? '))
excede = salario * 0.3
prestacao = valor / anos

if prestacao > excede:
    print('Não e possivel realizar o emprestimo')
elif prestacao < excede:
    print('E possivel realizar o emprestimo!!\nValor das prestacoes: {}'.format(prestacao))

