from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\nSua opcao: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos numeros e: {}'.format(soma))
    elif opcao == 2:
        mult = n1 * n2
        print('O valor da multiplicacao dos numeros e: {}'.format(mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior numero e: {}'.format(maior))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('opcao invalida!')
    print('=-=' * 10)
    sleep(1)
print('FIM!')