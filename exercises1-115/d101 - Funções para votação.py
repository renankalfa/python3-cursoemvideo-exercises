def voto(ano_nasc):
    from datetime import date
    idade = date.today().year - ano_nasc
    print(f'Você tem {idade}. \n'
          f'Situação de voto:', end=' ')
    if idade >= 16:
        if idade > 70 or 16 <= idade < 18:
            return print('\033[33mVOTO FACULTATIVO!\033[m')
        if 18 <= idade <= 70:
            return print('\033[32mVOTO OBRIGATÓRIO!\033[m')
        return
    return print('\033[31mVOTO NEGADO!\033[m')


voto(int(input('Ano de nascimento: ')))
