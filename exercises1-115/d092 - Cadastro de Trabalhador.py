from datetime import date
all = dict()
all['Nome'] = str(input('Digite o seu nome: '))
ano_nasc = int(input('Data de nascimento: '))
all['Idade'] = date.today().year - ano_nasc
all['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if all['Carteira de Trabalho'] != 0:
    all['Ano de contratação'] = int(input('Ano de contratação: '))
    all['Idade de aposentadoria'] = all['Idade'] + (35 - (date.today().year - all['Ano de contratação']))
    all['Salário'] = float(input('Salário: R$ '))
print('=' * 60)
print(f'{"Ficha Técnica":^60}')
print('=' * 60)
for key, value in all.items():
    print(f'{key}: {value}')
