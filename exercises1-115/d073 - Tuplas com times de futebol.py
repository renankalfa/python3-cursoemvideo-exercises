cbf = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('=!' * 30)
print(f'Lista de times do Brasileirão: {cbf}')
print('=!' * 30)
print(f'5 primeiros colocados: {cbf[:5]}')
print('=!' * 30)
print(f'últimos 4 colocados: {cbf[16:]}')
print('=!' * 30)
print(f'Lista de times em ordem alfabética: {sorted(cbf)}')
print('=!' * 30)
position = cbf.index('Chapecoense')
print(f'Chapecoense está na {position}° Posição. ')
