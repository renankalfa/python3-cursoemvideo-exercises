soma = 0

for c in range(0,6):
    numero = int(input('Insira o número: '))
    if numero % 2 == 0:
        soma = soma + numero
print(f'A soma dos números pares digitados é \033[31m{soma}.')