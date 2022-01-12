def menu(*lista):
    from time import sleep
    sleep(0.5)
    formatar('menu principal')
    cont = 1
    for c in lista:
        sleep(0.3)
        print(f'\033[33m{cont}\033[m - \033[36m{c}\033[m')
        cont += 1
    sleep(0.5)
    print('=' * 40)


def encerrar():
    from time import sleep
    sleep(0.3)
    print('\033[31m', end='')
    formatar('PROGRAMA encerrado')
    print('\033[m')


def formatar(frase='FRASE TESTE'):
    print('=' * 40)
    print(f'{frase.center(40).upper()}')
    print('=' * 40)
