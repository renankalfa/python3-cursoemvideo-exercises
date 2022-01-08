num = int(input('\033[31mInsira um número inteiro: \033[m'))
print('''Escolha uma das bases:
\033[35m[1] converter para BINÁRIO
\033[33m[2] Converter para OCTAL
\033[34m[3] converter para HEXADECIMAL \033[m''')
base = int(input('Sua opção: '))

if base == 1:
    print(f'{num} convertido para BINÁRIO é: {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para OCTAL é: {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido para HEXADECIMAL é: {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente!')