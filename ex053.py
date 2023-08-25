s = 'o'
while s != 'M' and s != 'F':
    s = str(input('Digite o seu sexo [M/F]: ')).upper()
    if s != 'M' and s != 'F':
        print('Digite um sexo valido! [M/F]')
print('FIM!')