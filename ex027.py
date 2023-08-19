km = float(input('Qual e a distancia da viagem? '))
if km <= 200:
    passagem =  0.5 * km
    print('o valor da passagem e: R${:.2f}'.format(passagem))
else:
    passagem = 0.45 * km
    print('o valor da passagem e: R${:.2f}'.format(passagem))
