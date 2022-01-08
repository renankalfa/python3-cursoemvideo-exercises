from time import sleep


def maior(*lista):
    print('=' * 33)
    print('Analisando os valores passados...')
    try:
        maiorn = max(lista)
    except ValueError:
        maiorn = 0
    for number in lista:
        sleep(0.5)
        print(number, end=' ')
    print(f'Foram informados {len(lista)} valores. \n'
          f'O maior valor encontrado foi {maiorn}.')


maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
