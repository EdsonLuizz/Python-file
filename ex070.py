import random
lista = random.randint(0, 10), random.randint(0,10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
for c in lista:
    print(f'{c} ', end ='')
print(f'\n{max(lista)} e o maior numero')
print(f'{min(lista)} e o menor numero')