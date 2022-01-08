sal = float(input('Salário do funcionário: '))

if sal > 1250.00:
    sal1 = sal * 1.1
    print(f'O salário será de R${sal1:.2f}.')
else:
    sal2 = sal * 1.15
    print(f'O salário é de {sal2:.2f} reais.')
