import math

a = float(input('Comprimento 1: '))
b = float(input('Comprimento 2: '))
c = float(input('Comprimento 3: '))

if math.fabs(b - c) < a < b + c:
    print(f'O triângulo formado por {a:.1f}, {b:.1f} e {c:.1f} é possível de ser formado.')
    if a == b and a == c:
        print('\033[31mO triângulo é EQUILÁTERO!')
    elif a == b or a == c:
        print('\033[32mO triângulo é ISÓSCELES!')
    else:
        print('\033[33mO triângulo é ESCALENO!')
else:
    print('Não é possível formar o triângulo!')