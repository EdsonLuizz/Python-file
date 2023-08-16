import math
op = float (input('Diga o comprimento do cateto oposto: '))
adj = float (input('Diga o comprimento do cateto adjacente: '))
hipo = math.hypot(op, adj)
print('hipotenusa: {:.2f}'.format(hipo))
