from random import randint
numbers = list()


def sorteia():
    print('Sorteando 5 valores: ', end='')
    for c in range(5):
        sorted_number = randint(0, 10)
        print(sorted_number, end=' ')
        numbers.append(sorted_number)
    print('Sorteio encerrado.')


def somaPar():
    print(f'Somando os números pares de {numbers}, temos ', end='')
    s_p = 0
    for numero in numbers:
        if numero % 2 == 0:
            s_p += numero
    print(f'{s_p}.')


sorteia()
somaPar()