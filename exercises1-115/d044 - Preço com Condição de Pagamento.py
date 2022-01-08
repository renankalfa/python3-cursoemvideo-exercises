price = float(input('Preço do produto: R$ '))
print('''Condição de pagamento:
[1] À vista no dinheiro
[2] À vista no Cartão
[3] 2x no Cartão
[4] 3x ou mais no Cartão''')

option = int(input('Digite o número que corresponde a opção de pagamento: '))

if option == 1:
    new_price = price * 0.90
    print(f'Preço com desconto: R${new_price:.2f}.')
elif option == 2:
    new_price = price * 0.95
    print(f'Preço com desconto à vista no cartão: R${new_price:.2f}.')
elif option == 3:
    parcela = price / 2
    print(f'Preço em duas vezes no cartão: R${price}, com duas parcelas de R${parcela:.2f}.')
elif option == 4:
    total = price * 1.2
    n_parcelas = int(input('Número de parcelas: '))
    parcela = total / n_parcelas
    print(f'Preço final: R${total:.2f} \nPreço das parcelas: R${parcela:.2f}.')
else:
    print('Opção inválida. Tente novamente!')