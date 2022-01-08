import random
count_wins = cont = 0

while True:
    pc = random.randint(0, 10)
    eu = int(input('Digite um valor: '))
    eu_opcao = str(input('Par ou ímpar [P/I]: ')).upper()
    soma = pc + eu
    cont += 1
    if soma % 2 == 0:
        print(f'Você escolheu {eu} e o computador {pc}. A soma deu {soma} e o resultado é PAR!')
        if eu_opcao == 'P':
            count_wins += 1
        else:
            print('Você perdeu!')
            break
    else:
        print(f'Você escolheu {eu} e o computador {pc}. A soma deu {soma} e o resultado é ÍMPAR!')
        if eu_opcao == 'I':
            count_wins += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente!')
print(f'Você jogou {cont} vezes e venceu {count_wins} vezes.')