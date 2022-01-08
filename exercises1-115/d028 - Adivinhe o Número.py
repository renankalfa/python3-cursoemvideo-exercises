import random

sorteio = random.randint(0, 5)

adivinha = int(input('Escolha um número de 0 à 5: '))

print(f'O número sorteado pelo máquina foi {sorteio}. \nE o seu número foi {adivinha}.')

if adivinha == sorteio:
    print('Você é o cara da adivinhação!')
else:
    print('Você eroouuu!')