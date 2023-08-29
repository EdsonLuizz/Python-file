total = 0
caros = 0
resp = 's'
menor = 0
cont = 0
barato = ''
while resp == 's':
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    if preco > 1000:
        caros += 1
    resp = str(input('Quer continuar?[s/n]')).lower()
print(f'\nO total gasto foi R${total:.2f}')
print(f'{caros} produtos custam mais de R$1000')
print(f'Produto mais barato: {barato} custando R${menor:.2f}')