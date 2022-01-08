name_n1n2 = [[], [], []]
count = peopleid = 0
while True:
    name_n1n2[0].append(str(input(f'Digite o nome do {count + 1}° aluno: ')))
    name_n1n2[1].append(float(input('Primeira nota: ')))
    name_n1n2[2].append(float(input('Segunda nota: ')))
    count += 1
    option = str(input('Você que continuar [S/N]? ')).upper()
    while option not in 'SN':
        option = str(input('\033[31m Erro! Você quer continar [S/N]? \033[m')).upper()
    if option == 'N':
        break

print('=' * 28)
print('N°  Nome           Média')
print('-' * 28)
for c in name_n1n2[0]:
    print(f'{peopleid:<4}{c:<15}{(name_n1n2[1][peopleid] + name_n1n2[2][peopleid])/2:.2f}')
    peopleid += 1
print('-' * 28)
while True:
    option1 = int(input('Qual número do aluno você deseja ver a nota (99 para parar)? '))
    if option1 == 99:
        break
    else:
        print(f'Notas do aluno {name_n1n2[0][option1]}: \n'
              f'Primeira nota: {name_n1n2[1][option1]:.2f}; \n'
              f'Segunda nota: {name_n1n2[2][option1]:.2f}.')
    print('-' * 28)