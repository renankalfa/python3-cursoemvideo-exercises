numbers = ('zero','um','dois','três','quatro','cinco', 'seis',
            'sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    option = int(input('Escolha um número (999 para parar): '))
    if option == 999:
        break
    while option < 0 or option > 20:
        option = int(input('Tente novamente! \nEscolha um número: '))
    print(f'Você escolheu o número \033[31m{numbers[option]}\033[m ({option}).')
print('Programa encerrado. Volte sempre!')
