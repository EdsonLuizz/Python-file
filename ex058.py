n = int(input('Digite o primeiro valor da PA: '))
r = int(input('Digite a razao: '))
termo = n
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} => '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quanto termos voce quer mostrar a mais? '))
print('FIM')
