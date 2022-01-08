numero = int(input('Número: '))
cont = 0

if numero > 1:
    for c in range(1, numero + 1):
        divisao = numero % c
        if divisao == 0:
            cont = cont +1
    if cont == 2:
        print(f'O número {numero} é PRIMO')
    else:
        print(f'O número {numero} não é PRIMO')