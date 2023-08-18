v = int(input('digite a velocidade do carro: '))
multa = (v % 80) * 7
if v > 80:
    print('voce foi multado!!')
    print('preco da multa: {}R$'.format(multa))

