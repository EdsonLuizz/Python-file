v = 0
m = 0
media = 0
for c in range (0, 4):
    nome = str(input('Qual o seu nome? ')).lower()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ').lower())
    media = media + idade
    if idade > v and sexo == 'masculino':
        v = idade
        nomev = nome
    if sexo == 'feminino' and idade < 20:
        m = m + 1
print('A media de idade e {:.1f}\nO nome do homem mais velho e: {}\nTem {} mulheres no grupo com menos de 20 anos'.format(media / 4, nomev, m))