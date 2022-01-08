import datetime
contador = 0
atual = datetime.datetime.today().year
maior = 0
menor = 0

for c in range(1, 8):
    anos = int(input(f'Ano da {c}° pessoa: '))
    idade = atual - anos
    if idade >= 18:
        maior = maior + 1
    elif 18 > idade >= 0:
        menor = menor + 1

print(f'Quantidade de pessoas maiores de idade: {maior} \nQuantidade de pessoas menores de idade: {menor}')
