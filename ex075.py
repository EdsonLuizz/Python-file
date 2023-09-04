num = []
resp = 's'
while resp != 'n':
    t = int(input('Digite um valor: '))
    if t in num:
        print('Este numero ja existe na lista!! Numero não adicionado!!')
    else:
        num.append(t)
        print('Numero adicionado com sucesso!!')
    resp = str(input('Quer continuar? [S/N] ')).lower()
    while resp != 'n' and resp != 's':
        resp = str(input('Quer continuar? [S/N] ')).lower()
num.sort()
print(f'Voce digitou os valores: {num}')