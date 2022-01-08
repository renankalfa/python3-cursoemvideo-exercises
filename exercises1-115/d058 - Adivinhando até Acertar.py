from random import randint
pc_number = randint(0,10)
palpites = 1
jogador = int(input('Tente adivinhar o número sorteado: '))

while jogador != pc_number:
    print('\033[31mComputador: VOCÊ ERROU!!\033[m')
    palpites += 1
    jogador = int(input('Tente novamente: '))

print(f'Você acertou! Foram necessários {palpites} palpites. '
      f'\nO computador escolheu o {pc_number} e você o {jogador}.')