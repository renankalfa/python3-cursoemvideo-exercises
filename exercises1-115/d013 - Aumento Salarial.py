print('Aumento/Diminuição Salarial')
sa = float(input('Salário a ser aumentado (em R$): '))
print('Obs: \n 1. Coloque apenas o número sem a "%". \n 2. Em casos de diminuição, escreva-o com o sinal de menos.')
a = float(input('Aumento/Diminuição Salarial: '))
sr = sa * ((100 + a) / 100)
print(f'Salário reajustado: {sr}')