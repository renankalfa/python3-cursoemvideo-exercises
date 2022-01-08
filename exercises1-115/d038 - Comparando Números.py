num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print(f'\033[31mO número {num1} é maior que o {num2}.')
elif num2 > num1:
    print(f'\033[32mO número {num2} é maior que o {num1}.')
else:
    print(f'Os números são iguais!')
