from random import randint

#Início
print('=*'*5, 'Jokenpô', '=*' * 5)
print('''[1] Pedra
[2] Papel
[3] Tesoura''')

#Variáveis
jogador = int(input('Escolha um: '))
computador = randint(1, 3)

#Jogador escolhe Pedra
if jogador == 1 and computador == 2:
    print(f'Jogador: Pedra \nComputador: Papel \n\033[31mComputador venceu!')
elif jogador == 1 and computador == 3:
    print(f'Jogador: Pedra \nComputador: Tesoura \n\033[32mVocê venceu!')
elif jogador == 1 and computador == 1:
    print(f'Jogador: Pedra \nComputador: Pedra \n\033[33mEmpate!')

#Jogador escolhe Papel
elif jogador == 2 and computador == 1:
    print(f'Jogador: Papel \nComputador: Pedra \n\033[32mVocê venceu!')
elif jogador == 2 and computador == 3:
    print(f'Jogador: Papel \nComputador: Tesoura \n\033[31mComputador perdeu!')
elif jogador == 2 and computador == 2:
    print(f'Jogador: Papel \nComputador: Papel \n\033[33mEmpate!')

#Jogador escolhe a Tesoura
elif jogador == 3 and computador == 1:
    print(f'Jogador: Tesoura \nComputador: Pedra \n\033[31mComputador venceu!')
elif jogador == 3 and computador == 2:
    print(f'Jogador: Tesoura \nComputador: Papel \n\033[32mVocê venceu!')
elif jogador == 3 and computador == 3:
    print(f'Jogador: Tesoura \nComputador: Tesoura \n\033[33mEmpate!')

else:
    print('Opção inválida!')