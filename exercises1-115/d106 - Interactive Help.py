def adaptformat(text='Acessando o manual do comando', forb='print'):
    frase = f'{text} {forb}'
    size = len(frase) + 2
    print('\033[44m=' * size)
    print(f'{frase:^{size}}')
    print('=' * size)
    print('\033[m', end='')


def menuhelp():
    print('\033[42m=' * 30)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print('=' * 30)
    print('\033[m', end='')


def finddoc(opt):
    from time import sleep
    sleep(1)
    adaptformat(forb=opt)
    sleep(1)
    print('\033[40m')
    help(opt)
    print('\033[m', end='')


# Programa Principal
cont = 0
while True:
    from time import sleep
    if cont < 1:
        sleep(1)
    else:
        sleep(4)
    cont += 1
    menuhelp()
    sleep(0.5)
    option = str(input('Função ou Biblioteca -> '))
    finddoc(option)
