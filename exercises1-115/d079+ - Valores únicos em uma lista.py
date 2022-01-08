lista = []
count = 0
while True:
    count += 1
    n1 = int(input(f'Digite o {count}° número: '))
    if count != 1:
        if n1 in lista:
            while n1 in lista:
                n1 = int(input(f'\033[31mErro! Número duplicado. Tente novamente digitar o {count}° número: \033[m'))
                if n1 not in lista:
                    lista.append(n1)
                    break
        else:
            lista.append(n1)
    else:
        lista.append(n1)
    option = str(input('Você quer continuar [S/N]? ')).upper()
    while option not in 'SN':
        option = str(input('\033[31mOpção inválida! Você quer continuar [S/N]? \033[m')).upper()
    if option in 'Nn':
        break
lista.sort()
print(f'Lista final (ordenada): {lista}')
