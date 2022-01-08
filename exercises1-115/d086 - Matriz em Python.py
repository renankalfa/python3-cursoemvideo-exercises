princ = [[],[],[]]
countl = countt = countl1 = countt1 = 0

for c in range(9):
    if 6 > c > 2:
        countl = 1
        if c == 3:
            countt = 0
    if c >= 6:
        countl = 2
        if c == 6:
            countt = 0
    n1 = int(input(f'Digite um número para a posição [{countl}, {countt}]: '))
    princ[countl].append(n1)
    countt += 1

for pos, l in enumerate(princ):
    for p in l:
        print(f'[{p:^5}]', end=' ')
    print()
