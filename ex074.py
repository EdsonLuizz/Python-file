num = []
maior = 0
menor = 0
for c in range(0, 5):
    num.append(int(input('Digite um numero: ')))
    if c == 0:
        menor = maior = num[0]
    else:
        if menor > num[c]:
            menor = num[c]
        if maior < num[c]:
            maior = num[c]

print('=-'*20)
print(f'Valores digitados {num}')
print(f'O maior valor digitado foi: {maior} e ele foi encontrado na posição', end='')
for c, v in enumerate(num):
    if v == maior:
        print(f' {c + 1}....')
print(f'O menor valor digitado foi: {menor} e ele foi encontrado na posição', end='')
for i, f in enumerate(num):
    if f == menor:
        print(f' {i + 1}...')