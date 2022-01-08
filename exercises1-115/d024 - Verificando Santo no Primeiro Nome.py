n = str(input('Insira o nome de uma Cidade: '))
print(f'O nome escolhido foi {n} \nVerificando se começa com "Santo"...')
ns = n.split()

print('Santo' in ns[0])