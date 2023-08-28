n = 1
while n > 0:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        print('Finalizando programa...')
        break
    else:
        for c in range(1, 11):
            print('{} x {} = {}'.format(n, c, n * c))
