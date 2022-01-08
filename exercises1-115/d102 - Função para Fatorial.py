def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número (num) dado
    :param num: número a ser calculado o fatorial
    :param show: se deve ou não mostrar o cálculo do fatorial
    :return: fatorial
    """
    f = 1
    print('=' * 30)
    for c in range(num, 0, -1):
        f *= c
        if show is True:
            if c > 1:
                print(f'{c} x', end=" ")
            else:
                print(f'{c} =', end=" ")
    return print(f)


fatorial(3, False)
fatorial(4, True)
fatorial(int(input('Digite um número: ')), True)
help(fatorial)
