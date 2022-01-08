from math import radians, sin, cos, tan

#Variáveis e Cálculos (Ele lê em radianos)

a = float(input('Insira um ângulo (graus): '))
g = radians(a)
s = sin(g)
c = cos(g)
t = tan(g)

#Tela

print(f'O seno vale {s:.2f}, o cosseno vale {c:.2f} e a tangente vale {t:.2f}.')