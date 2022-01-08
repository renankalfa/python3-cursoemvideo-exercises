jogadores = list()
jogador = dict()
gols = list()
gols_totais = list()
soma_gols = id = c_partidas = 0

while True:
    print('-' * 36)
    jogador['Nome'] = str(input('Nome do jogador: '))
    q_partidas = int(input('Quantas partidas foram jogadas? '))
    for number in range(q_partidas):
        gol = int(input(f'Quantidade de gols na {number + 1}° Partida: '))
        gols.append(gol)
        soma_gols += gol
    jogador['Gols'] = gols[:]
    jogador['Gols Totais'] = soma_gols
    soma_gols = 0
    gols.clear()
    option = str(input('Você quer continuar [S/N]? ')).upper()
    jogadores.append(jogador.copy())
    while option not in 'SN':
        option = str(input('\033[31mTente novamente! Você quer continuar [S/N]? \033[m')).upper()
    if option == 'N':
        break

print()
print('=-' * 23)
print(f'cod {"nome":>6} {"gols":>13} {"total":>14}')
print('=-' * 23)
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end='')
    for value in v.values():
        print(f'   {str(value):<11}', end='')
    print()
    id += 1
print('=-' * 23)

while True:
    option_id = int(input('Mostrar dados de qual jogador [id]? '))
    print('=-' * 23)
    if option_id == 999:
        break
    if option_id >= len(jogadores):
        print('\033[31mErro! Tente novamente!\033[m')
        print('=-' * 23)
    else:
        print(f'Levantamento do jogador {jogadores[option_id]["Nome"]}:')
        for goal in jogadores[option_id]['Gols']:
            c_partidas += 1
            print(f'-> Na {c_partidas}° Partida, {goal} gols foram feitos.')
        print(f'Dando um total de {jogadores[option_id]["Gols Totais"]} gols feitos.')
        print('-' * 38)
        c_partidas = 0
print('\033[31mPrograma encerrado!\033[m')
