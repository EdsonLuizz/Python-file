r1 = float(input('r1: '))
r2 = float(input('r2: '))
r3 = float(input('r3: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('E possivel formar um triangulo!!\n')
    if r1 == r2 == r3:
        print('Triangulo Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isosceles')
else:
    print('Nao e possivel formar um triangulo!!')
