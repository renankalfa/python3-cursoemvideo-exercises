from time import sleep


def contador(inicio, fim, passo):
    print('=-' * 17)
    print(f'Contador de {inicio} até {fim}, de {passo if passo != 0 else 1} em '
          f'{passo if passo != 0 else 1}:\033[31m')
    number = inicio
    if inicio < fim:
        if passo == 0:
            passo = 1
        while number <= fim:
            sleep(0.5)
            print(number, end=' ')
            number += abs(passo)
        sleep(0.5)
        print('Fim!\033[m')
    elif inicio > fim:
        if passo == 0:
            passo = 1
        while number >= fim:
            sleep(0.5)
            print(number, end=' ')
            number -= abs(passo)
        sleep(0.5)
        print('Fim!\033[m')


contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 30)
print(f'{"Contagem personalizada":^30}')
print('=' * 30)
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
