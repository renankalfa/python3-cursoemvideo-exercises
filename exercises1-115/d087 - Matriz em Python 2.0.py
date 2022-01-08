princ = [[], [], []]
countl = countt = countl1 = countt1 = somap = somai = soma3 = max2 = 0

for c in range(9):
    if 6 > c > 2:
        countl = 1
        if c == 3:
            countt = 0
    if c >= 6:
        countl = 2
        if c == 6:
            countt = 0
    n1 = int(input(f'Digite um valor para [{countl}, {countt}]: '))
    princ[countl].append(n1)
    countt += 1
print('=' * 21)

for pos, linha in enumerate(princ):
    if pos == 1:
        max2 = max(linha)
    for pos1, p in enumerate(linha):
        print(f'[{p:^5}]', end='')
        if p % 2 == 0:
            somap += p
        if pos1 == 2:
            soma3 += p
    print()
print('=' * 21)

print(f'a) Soma de todos os valores pares: {somap}. \n'
      f'b) Soma dos valores da terceira coluna: {soma3}. \n'
      f'c) Maior valor da segunda linha: {max2}.')
