perfil = dict()
list_gols = list()
soma = count = 0
perfil['Nome'] = str(input('Nome: '))
q_par = int(input('Quantas partidas foram jogadas? '))
for c in range(q_par):
    n1 = int(input(f'Quantos gols na {c + 1}° partida? '))
    list_gols.append(n1)
    soma += n1
perfil['Gols'] = list_gols.copy()
perfil['Gols Totais'] = soma
print('=' * 33)
for k, v in perfil.items():
    print(f'{k}: {v}.')
print('=' * 33)
print(f'O jogador {perfil["Nome"]} jogou {q_par} partidas.')
for c in perfil['Gols']:
    count += 1
    print(f'{"=>":>6} Na {count}° partida, fez {c} gols.')
