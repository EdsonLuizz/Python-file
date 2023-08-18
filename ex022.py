f = str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {}vez(es)'.format(f.count('a')))
print('A posicao que a letra A aparece pela primeira vez e: {}'.format(f.find('a')+1))
print('A ultima vez que a letra A aparece e: {}'.format(f.rfind('a')+1))
