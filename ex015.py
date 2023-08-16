import math
a = float(input('Digite o valor do angulo: '))
cos = math.cos(math.radians(a))
sen = math.sin(math.radians(a))
tang = math.tan(math.radians(a))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sen, cos, tang))