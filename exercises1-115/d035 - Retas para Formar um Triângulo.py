import math

r1 = int(input('Comprimento da reta 1 (cm): '))
r2 = int(input('Comprimento da reta 2 (cm): '))
r3 = int(input('Comprimento da reta 3 (cm): '))

print(f'\nAs retas possuem comprimento de {r1} cm, {r2} cm e {r3} cm.')

if (math.fabs(r2 - r3) < r1 < r2 + r3):
    print('Podem formar um triângulo.')
else:
    print('Não podem formar um triângulo.')