def ficha(nome="", gols=""):
    if nome.strip() == '':
        nome = '\033[31mDesconhecido\033[m'
    if gols == '':
        gols = 0
    else:
        if not gols.isdecimal():
            gols = 0
    print('=' * 40)
    print(f'O jogador {nome.capitalize()} fez {gols} gol(s).')
    print('=' * 40)


ficha(input('Nome do jogador: '), input('Gols: '))
