n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

lista = [n1, n2, n3]
#Maiores números
if n1 > n2:
    if n1 > n3:
        print(f'Maior número: {n1}')
if n2 > n1:
    if n2 > n3:
        print(f'Maior número: {n2}')
if n3 > n1:
    if n3 > n2:
        print(f'Maior número: {n3}')
#Menores números
if n1 < n2:
    if n1 < n3:
        print(f'Menor número: {n1}')
if n2 < n1:
    if n2 < n3:
        print(f'Menor número: {n2}')
if n3 < n2:
    if n3 < n1:
        print(f'Menor número: {n3}')