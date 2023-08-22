preco = float(input('Qual e o valor do produto? '))
opcao = int(input('\nQual a forma de pagamento?\n1- À vista (dinheiro/cheque)\n2- À vista no cartao\n3- Em ate 2x no cartao\n4- 3x ou mais no cartao\nSua opcao: '))
if opcao == 1:
    desconto1 = preco * 0.10
    valor1 = preco - desconto1
    print('\nVoce ganhou 10% de desconto!')
    print('Novo valor a ser pago: R${:.2f}'.format(valor1))
elif opcao == 2:
    desconto2 = preco * 0.05
    valor2 = preco - desconto2
    print('\nVoce ganhou 5% de desconto')
    print('Novo valor a ser pago: R${:.2f}'.format(valor2))
elif opcao == 3:
    print('\nValor normal')
    print('Valor a ser pago: R${:.2f}'.format(preco))
else:
    parcelas = int(input('Qual e o numero de parcelas? '))
    juros = preco * 0.20
    valorparcelado = (preco + juros) / parcelas
    valor3 = preco + juros
    print('\nSua compra sera parcelada em {}x de R${}'.format(parcelas, valorparcelado))
    print('Novo valor a ser pago: R${:.2f}'.format(valor3))