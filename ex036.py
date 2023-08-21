nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print('Sua media foi: {}'.format(media))
if media < 5:
    print('voce esta REPROVADO')
elif media >= 5 and media <= 6.9:
    print('voce esta RECUPERACAO')
else:
    print('voce esta APROVADO')
