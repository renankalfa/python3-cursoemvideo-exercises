def Área():
    largura = float(input('Largura (metros): '))
    comprimento = float(input('Comprimento (metros): '))
    area = largura * comprimento
    print(f'\033[32mÁrea do terreno: {area:.2f}m²\033[m')


def Cabeçalho():
    print('=' * 33)
    print(f'{"Controle de Terrenos":^33}')
    print('=' * 33)


while True:
    Cabeçalho()
    Área()
    print('-' * 33)
    option = str(input('Você quer continuar [S/N]? ')).upper()
    while option not in 'SN':
        option = str(input('\033[31mTente novamente! Você quer continuar [S/N]? \033[m')).upper()
    if option == 'N':
        break

print('=' * 33)
print('\033[31mPrograma Encerrado! Volte sempre!\033[31m')
