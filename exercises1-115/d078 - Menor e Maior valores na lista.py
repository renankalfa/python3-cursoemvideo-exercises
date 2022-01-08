numbers = []
for count in range(5):
    numbers.append(int(input(f'Digite o {count + 1} número: ')))
print('=-' * 30)
print(f'Você digitou os valores {numbers}')

#Maior valor:
print(f'O maior valor digitado foi {max(numbers)} nas posições ', end='')
for pos, v in enumerate(numbers):
    if v == max(numbers):
        print(pos, end='... ')
#Menor valor:
print(f'\nO menor valor digitado foi {min(numbers)} nas posições ', end='')
for p, f in enumerate(numbers):
    if f == min(numbers):
        print(p, end='... ')
