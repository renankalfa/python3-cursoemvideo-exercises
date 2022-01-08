princ = [[],[]]

for c in range(7):
    n1 = int(input(f'Digite o {c + 1}° número: '))
    if n1 % 2 == 0:
        princ[0].append(n1)
    else:
        princ[1].append(n1)
princ[0].sort()
princ[1].sort()

print(f'Números pares: {princ[0]}. \nNúmeros ímpares: {princ[1]}.')
