def leiaInt(frase='Digite um número inteiro: '):
    from time import sleep
    while True:
        try:
            n = int(input(frase))
        except (ValueError, TypeError):
            print('\033[31mErro de valor! Digite um número do tipo inteiro.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar o número.\033[m')
            sleep(1)
            return 0
        else:
            return n


def leiaFloat(frase='Número real: '):
    from time import sleep
    while True:
        try:
            n = float(input(frase))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar o número.\033[m')
            sleep(1)
            return 0
        else:
            return n


print('=' * 48)
n1 = leiaInt('Número inteiro: ')
n2 = leiaFloat('Número real: ')
print('=' * 48)
print(f'Número inteiro digitado foi \033[31m{n1}\033[m e o real \033[31m{n2:.2f}\033[m')
print('=' * 48)
