from time import sleep
print('='*30)
print('Contrução de Cardápio de Bares')
print('='*30)

nome_do_bar = str(input('Qual nome de bar você deseja usar? '))
quantidade_de_pratos = int(input('Qual a quantidade de pratos você deseja cadastrar? '))
name_price = ()
ct = 0
for c in range(quantidade_de_pratos):
    ct += 1
    prato = str(input(f'Nome do {ct}° prato a cadastrar: '))
    price = float(input(f'Preço do {ct}° prato a cadastrar: '))
    name_price += (prato, price)

# Contadores e Strings definidas
count = 0
count2 = 1

# Design e detalhes do MENU
estabelecimento = nome_do_bar
print('='*30)
print(estabelecimento.center(30, ' '))
print('='*30)

# Estrutura que cria o MENU
while True:
    sleep(0.6)
    print(f'{name_price[count]:.<20}R$ {name_price[count2]:>6}')
    count += 2
    count2 += 2
    if count2 >= len(name_price):
        break
print('='*30)
