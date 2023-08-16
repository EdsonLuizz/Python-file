d = int (input('Quantos dias o veiculo foi alugado? '))
km = float (input('Quantos km rodados? '))
cc = d * 60
ckm = km * 0.15
soma = cc + ckm
print('O valor total e: {}'.format(soma))
