from datetime import date

nascimento = int(input('Ano de nascimento do atleta: '))
hoje = date.today().year
idade = hoje - nascimento
print(f'Você nasceu no ano de {nascimento} e tem {idade} anos.')

if 0 < idade <= 9:
    print('classificação MIRIM')
elif 9 < idade <= 14:
    print('classificação INFANTIL')
elif 14 < idade <= 19:
    print('classficação JUNIOR')
elif 19 < idade <= 20:
    print('classficação SENIOR')
elif 150 > idade > 20:
    print('classificação MASTER')
else:
    print('Error 404: Idade irreal')