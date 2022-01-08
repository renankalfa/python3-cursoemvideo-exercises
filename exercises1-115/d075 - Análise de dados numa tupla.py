numbers = tuple(int(input('Digite um número: ')) for c in range(4))
count_par = 0
for c in numbers:
    if c % 2 == 0:
        count_par += 1
print(f'\033[31mAnálise de dados \033[m \n'
      f'a) O número 9 apareceu {numbers.count(9)} vezes.')
print(f'b) O primeiro 3 apareceu na {numbers.index(3) + 1}° Posição.' if 3 in numbers else 'b) O número 3 não foi digitado.')
print(f'c) Quantidade de números pares: {count_par}.')
