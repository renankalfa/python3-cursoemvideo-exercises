import random, time
t = int(input('Quantos jogos serão sorteados? '))
for c in range(t):
    lista_gerada = random.sample(range(1, 60), k=6)
    time.sleep(0.5)
    print(f'{c + 1}° Lista de números gerada: {lista_gerada}')
