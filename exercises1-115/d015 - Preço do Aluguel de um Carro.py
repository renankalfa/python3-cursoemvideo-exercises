print('Preço do Aluguel do Carro')
km = float(input('Quantidade de quilômetros percorrida: '))
dias = int(input('Quantidade de dias alugados: '))
pf = 60 * dias + 0.15 * km
print(f'\n Informações: \n Km rodados: {km}km \n Dias alugados: {dias:.0f} dias')
print(f'\n Será preciso pagar: R${pf:.2f}')