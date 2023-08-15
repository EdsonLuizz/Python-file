altura = float(input('digite a altura da parede: '))
largura = float(input('digite a largura da parede: '))
area = altura * largura
lt = area / 2
print('A area e: {}\nA quantidade de Litros de tinta necessaria para pintar tudo: {:.1f}l'.format(area, lt))