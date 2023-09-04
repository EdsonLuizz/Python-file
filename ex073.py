palavras = ('estudar', 'prova', 'minuscula')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos: ', end='')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end=' ')
