def leiaInt(frase):
    num = input(frase)
    while not num.isdecimal():
        print('\033[31mERRO! Digite um número inteiro.\033[m')
        num = input(frase)
    num = int(num)
    return num


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
