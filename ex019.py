n = int(input('digite um numero de 0 a 9999: '))
m = n // 1000
c = (n % 1000) // 100
d = ((n % 1000) % 100) // 10
u = ((n % 1000) % 100) % 10
print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(u, d, c, m))