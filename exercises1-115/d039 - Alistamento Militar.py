from datetime import date

nascimento = int(input('Ano de nascimento: '))
hoje = date.today().year
anos_pessoa = hoje - nascimento

if anos_pessoa < 18:
    alistar = hoje + (18 - anos_pessoa)
    print(f'Você deverá se alistar no ano de {alistar}! Aguarde até lá.')
elif anos_pessoa == 18:
    print('Chegou a hora de você se alistar!')
else:
    alistar = hoje - (anos_pessoa - 18)
    print(f'Você deveria ter se alistado em {alistar}. Já passou seu tempo!')