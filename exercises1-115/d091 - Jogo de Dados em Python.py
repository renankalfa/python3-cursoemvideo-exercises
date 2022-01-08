import random, time
geral = dict()
count = 1
geral1 = dict()
list = list()
for c in range(4):
    n1 = random.randint(1, 6)
    geral[f'Jogador{c + 1}'] = n1
time.sleep(0.5)
print('Dados jogados...')
for f, v in geral.items():
    time.sleep(0.5)
    print(f'  O {f} jogou {v}...')
for p in geral.values():
    list.append(p)
    list.sort()
for c in range(6):
    for k, v in geral.items():
        if v == (max(list) - c):
            geral1[f'{k}'] = f'{v}'
time.sleep(0.5)
print('Ranking dos jogadores:')
for k, v in geral1.items():
    time.sleep(0.5)
    print(f'  {count}°Lugar: {k} com o número {v}.')
    count += 1
