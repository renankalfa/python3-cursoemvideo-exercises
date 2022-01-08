count5 = count = 0
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    count += 1
    if 5 in lista:
        count5 += 1
    option = str(input('Você quer continuar [S/N]? ')).upper()
    while option not in 'SN':
        option = str(input('\033[31mTente novamente! Você quer continuar [S/N]? \033[m')).upper()
    if option == 'N':
        break
lista.sort(reverse=True)
print(f'Quantidade de elementos: {count}. \nLista em ordem decrescente: {lista}')
if count5 > 0:
    print(f'Quantidade de números 5 digitados: {count5}.')
else:
    print(f'\033[31mNenhum número 5 foi digitado.\033[m')
