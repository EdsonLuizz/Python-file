while True:
    valor = int(input('Qual valor deseja sacar? '))
    cem = valor // 100
    cinquenta = (valor % 100) // 50
    vinte = ((valor % 100) % 50) // 20
    dez = (((valor % 100) % 50) % 20) // 10
    dois = ((((valor % 100) % 50) % 20) % 10) // 2
    print(f'Total de {cem} cédulas de R$100')
    print(f'Total de {cinquenta} cédulas de R$50')
    print(f'Total de {vinte} cédulas de R$20')
    print(f'Total de {dez} cédulas de R$10')
    print(f'Total de {dois} cédulas de R$2')
    break