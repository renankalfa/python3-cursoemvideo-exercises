cp_1000 = 0
count = 1
name0 = str(input(f'Nome do {count}° produto: '))
price0 = float(input('Preço do produto: '))
if price0 > 1000:
    cp_1000 = 1
st = price0
resp = str(input('Você quer continuar [S/N]? '))
cheap = name0

while resp in 'Ss':
    count += 1
    name = str(input(f'Nome do {count}° produto: '))
    price = float(input('Preço do produto: '))
    st += price
    if price > 1000:
        cp_1000 += 1
    if price < price0:
        cheap = name
    price0 = price
    resp = str(input('Você quer continuar [S/N]? '))

print(f'a) Total gasto: R${st:.2f}. \nb) Quantidade de produtos que custam mais de 1000 reais: {cp_1000} \nc) Nome do produto mais barato: {cheap}')

#Refatorar usar while True: