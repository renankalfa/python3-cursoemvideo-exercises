lista_t = []
lista_i = []
lista_p = []

while True:
    n1 = int(input('Digite um valor: '))
    lista_t.append(n1)
    if n1 % 2 == 0:
        lista_p.append(n1)
    else:
        lista_i.append(n1)
    option = str(input('Você quer continuar [S/N]? ')).upper()
    while option not in 'SN':
        option = str(input('\033[31mTente novamente! Você quer continuar [S/N]? \033[m')).upper()
    if option == 'N':
        break
print(f'Lista total: {lista_t}; \nLista com número pares: {lista_p}; \nLista com números ímpares: {lista_i}.')
