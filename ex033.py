n = int(input('Digite um numero: '))
base = int(input('Digite a base da conversao:\n1-Binario\n2-Octal\n3-Hexa\nSua opcao: '))
if base == 1:
    print('o numero {} em BINARIO e: {}'.format(n, bin(n)[2:]))
elif base == 2:
    print('o numeoro {} em OCTAL e: {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('o numero {} em base HEXADECIMAL e: {}'.format(n, hex(n)[2:]))
else:
    print('opcao invalida!!')