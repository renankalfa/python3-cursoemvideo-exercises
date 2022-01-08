lista_pessoas = list()
pessoa = dict()
count = s_idade = dict_number = 0
while True:
    count += 1
    pessoa['Nome'] = str(input(f'Nome da {count}° Pessoa: '))
    pessoa['Sexo'] = str(input(f'Sexo da {count}° Pessoa [M/F]: ')).upper()
    pessoa['Idade'] = int(input(f'Idade da {count}° Pessoa: '))
    s_idade += pessoa['Idade']
    lista_pessoas.append(pessoa.copy())
    pessoa.clear()
    option = str(input('Você quer continuar [S/N]? ')).upper()
    while option not in 'SN':
        option = str(input('Tente novamente! Você quer continuar [S/N]? '))
    if option == 'N':
        break
print('=' * 40)
print(f'Quantidade de pessoas cadastradas: {count} \n'
      f'Média de idade do grupo: {s_idade / count:.2f} anos \n'
      f'Mulheres do grupo: ', end='')
for c in lista_pessoas:
    for k, v in c.items():
        if k == 'Sexo':
            if v == 'F':
                print(c["Nome"], end=' ')
print('\nPessoas com idade acima da média: ', end='')
for c in lista_pessoas:
    for k, v in c.items():
        if k == 'Idade':
            if v > (s_idade / count):
                print(c["Nome"], end =' ')
print()
print('=' * 40)