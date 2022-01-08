#Variáveis
nu = int(input('Insira um número de 0 a 9999: '))
print(f'Analisando o número {nu}...')

#Contas
u = nu % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000

#Mostrar
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')