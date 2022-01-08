number = int(input('Insira seu número: '))

par = [0, 2, 4, 6, 8]
impar = [1, 3, 5, 7, 9]

last = number % 10
print(last)

if last in par:
    print(f'O seu número {number} é par!')
else:
    print(f'O seu número {number} é ímpar!')

numero = int(input('Insira um número: '))


#Maneira 2, o resto da divisão de um número par por 2 é sempre 0, ímpar tem resto 1.
n = numero % 2

if n == 0:
    print('O número é par!')
else:
    print('O número é ímpar!')