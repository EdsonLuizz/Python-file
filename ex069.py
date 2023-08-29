times = 'BOTAFOGO', 'PALMEIRAS', 'GRÊMIO', 'FLAMENGO', 'FLUMINENSE', 'RED BULL BRAGANTINO', 'ATHLETICO-PR', 'FORTALEZA', 'ATLÉTICO-MG', 'CUIABÁ', 'SÃO PAULO', 'CRUZEIRO', 'CORINTHIANS', 'INTERNACIONAL', 'GOIÁS', 'BAHIA', 'SANTOS', 'VASCO', 'CORITIBA', 'AMÉRICA-MG'
print('OS 5 PRIMEIROS SAO:')
for c in range(0, 5):
    print(f'{c + 1} - {times[c]}')
print('=-' * 11)
print('OS 4 ULTIMOS SAO:')
for c in range(16,20):
    print(f'{c + 1} - {times[c]}')
print('=-' * 11)
print('TIMES ORDENADOS EM ORDEM ALFABETICA:')
print(sorted(times))
print('=-' * 11)
print('EM QUE POSICAO ESTA O VASCO?')
print(f'O Vasco esta na {times.index("VASCO")} posicao')