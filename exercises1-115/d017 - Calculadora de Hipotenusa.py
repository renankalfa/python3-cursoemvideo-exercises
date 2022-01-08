import math
co = float(input('Cateto Oposto (cm): '))
ca = float(input('Cateto Adjacente (cm): '))

#Duas formas de resolver

#h = math.sqrt(pow(co, 2) + pow(ca, 2))
h = math.hypot(co, ca)
print(f'A hipotenusa vale: {h:.2f}cm')
