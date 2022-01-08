print('=' * 20, '\n       NUBANK \n'+'=' * 20)
valor = int(input('Qual o valor a ser sacado? R$ '))
c50 = c20 = c10 = c1 = 0

while valor >= 50:
    c50 += 1
    valor -= 50
while valor >= 20:
    c20 += 1
    valor -= 20
while valor >= 10:
    c10 += 1
    valor -= 10
while valor >=1:
    c1 += 1
    valor -= 1

print(f'Cédulas de R$ 50,00: {c50} \nCédulas de R$ 20,00: {c20} \nCédulas de R$ 10,00: {c10} '
      f'\nCédulas de R$ 1,00: {c1}')
