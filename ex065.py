maioridade = 0
homem = 0
mulhermaior = 0
resp = 's'
while resp == 's':
    idade = int(input('Qual é a sua idade: '))
    if idade > 18:
        maioridade += 1
    sexo = 'p'
    while sexo != 'm' and sexo != 'f':
        sexo = str(input('Digite o seu sexo[m/f]: ')).lower()
    if sexo == 'm':
        homem += 1
    if sexo == 'f' and idade < 20:
        mulhermaior += 1
    r = 'x'
    while r != 's' and r != 'n':
        r = str(input('Quer continuar?[s/n] ')).lower()
    if r == 'n':
        break
print(f'Existem {maioridade} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homem} homem(ns)')
print(f'Existem {mulhermaior} mulheres abaixo de 20 anos')