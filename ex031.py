r1 = float(input('R1:'))
r2 = float(input('R2:'))
r3 = float(input('R3:'))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('e possivel formar um triangulo')
else:
    print('nao e possivel formar um triangulo')
