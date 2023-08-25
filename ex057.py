n = int(input('Digite o primeiro valor da PA: '))
r = int(input('Digite a razao: '))
termo = n
c = 1
while c <= 10:
    print('{} => '.format(termo), end='')
    termo += r
    c += 1
print('FIM')
