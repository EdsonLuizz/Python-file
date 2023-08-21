from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano
falta = idade - 18

if idade < 18:
    print('voce ainda deve se alistar\nfalta(m): {} ano(s)'.format(falta))
elif idade == 18:
    print('esta na hora de se alistar')
else:
    print('ja passou do tempo de alistamento\njá passou(ram) {} ano(s)'.format(falta))