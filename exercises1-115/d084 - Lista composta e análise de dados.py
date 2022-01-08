listag = []
peoplepeso = []
nomes = []
peso = []
countp = countpe = countl = 0

while True:
    countp += 1
    peoplepeso.append(str(input(f'Nome da {countp}° Pessoa: ')))
    peoplepeso.append(int(input(f'Peso da {countp}° Pessoa (Kg): ')))
    peso.append(peoplepeso[1])
    nomes.append(peoplepeso[0])
    listag.append(peoplepeso[:])
    peoplepeso.clear()
    option = str(input('Você quer continuar [S/N]? ')).upper()
    while option not in 'SN':
        option = str(input('\033[31mTente novamente! Você quer continuar [S/N]? ')).upper()
    if option == 'N':
        break

print(f'Pessoas cadastradas: {countp};')
print(f'O maior peso foi de {max(peso)}, com as pessoa(s) ', end='')
for c in peso:
    countpe += 1
    if c == max(peso):
        print(nomes[countpe - 1], end=' ')
print(f'\nO menor peso foi de {min(peso)}, com as pessoa(s) ', end='')
for c1 in peso:
    countl += 1
    if c1 == min(peso):
        print(nomes[countl - 1], end=' ')
