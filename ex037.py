from datetime import date
ano = int(input('Digite a idade do atleta: '))
idade = date.today().year - ano
print('idade: {} anos'.format(idade))
if idade <= 9:
    print('atleta MIRIM')
elif idade <= 14:
    print('atleta INFANTIL')
elif idade <= 19:
    print('atleta JUNIOR')
elif idade <= 20:
    print('atleta SENIOR')
else:
    print('atleta MASTER')
