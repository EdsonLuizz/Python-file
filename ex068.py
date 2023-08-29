while True:
    digito = int(input('digite um numero entre 0 e 20: '))
    if 0 > digito > 20:
        print('numero invalido!! Digite um numero entre 0 e 20')
    if 0 <= digito <= 20:
        break
numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
print(f'Voce digitou o numero {numeros[digito]}')
