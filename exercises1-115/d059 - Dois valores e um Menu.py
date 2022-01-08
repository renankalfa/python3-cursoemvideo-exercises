n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

print('*=' * 2, '\033[31mMenu de Opções\033[m', '*=' * 2
      , '\n[1] Somar \n[2] Multiplicar \n[3] Maior número \n[4] Novos Números \n[5] Sair do programa')
print('\033[32m=*\033[m' * 12)
option = int(input('Digite a sua opção: '))

while 0 < option < 5:
    if option == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
        print('*=' * 2, '\033[31mMenu de Opções\033[m', '*=' * 2
              , '\n[1] Somar \n[2] Multiplicar \n[3] Maior número \n[4] Novos Números \n[5] Sair do programa')
        print('\033[32m=*\033[m' * 12)
        option = int(input('Digite a sua opção: '))
    if option == 2:
        multi = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} è {multi}.')
        print('*=' * 2, '\033[31mMenu de Opções\033[m', '*=' * 2
              , '\n[1] Somar \n[2] Multiplicar \n[3] Maior número \n[4] Novos Números \n[5] Sair do programa')
        print('\033[32m=*\033[m' * 12)
        option = int(input('Digite a sua opção: '))
    if option == 3:
        maior = n1
        if n1 < n2:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}.')
        print('*=' * 2, '\033[31mMenu de Opções\033[m', '*=' * 2
              , '\n[1] Somar \n[2] Multiplicar \n[3] Maior número \n[4] Novos Números \n[5] Sair do programa')
        print('\033[32m=*\033[m' * 12)
        option = int(input('Digite a sua opção: '))
    if option == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print('*=' * 2, '\033[31mMenu de Opções\033[m', '*=' * 2
              , '\n[1] Somar \n[2] Multiplicar \n[3] Maior número \n[4] Novos Números \n[5] Sair do programa')
        print('\033[32m=*\033[m' * 12)
        option = int(input('Digite a sua opção: '))

print('\n\033[31mPrograma encerrado!\033[m')