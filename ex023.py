f = str(input('Digite o seu nome completo: ')).strip()
frase = f.split()
print('primerio nome: {}'.format(frase[0]))
print('ultimo nome: {}'.format(frase[len(frase)-1]))
