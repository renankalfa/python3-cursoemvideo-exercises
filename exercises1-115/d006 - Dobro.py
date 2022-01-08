#Tornando cada conta uma variável

n1 = int(input('Escolha um número: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print(f'Você escolheu o número {n1}. \n O seu dobro é {d}, \n O seu triplo é {t}, \n e a sua raiz quadrada é {r}.')
n = str(input('Eu acertei? '))
print('Eu acertei sim, não venha me zoar.')

# Sem tornar as contas uma nova variável

n1 = int(input('Escolha um número: '))
print(f'Você escolheu o número {n1}. \n O seu dobro é {n1*2}, \n O seu triplo é {n1*3}, \n e a sua raiz quadrada é {n1**(1/2)}.')
n = str(input('Eu acertei? '))
print('Eu acertei sim, não venha me zoar.')