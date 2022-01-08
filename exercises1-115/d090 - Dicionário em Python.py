ficha = dict()
ficha['Nome'] = str(input('Nome: ')).upper()
ficha['Média'] = float(input('Média: '))
if ficha['Média'] >= 7:
    ficha['Situação'] = 'Aprovado'.upper()
else:
    ficha['Situação'] = 'Reprovado'.upper()

for k, v in ficha.items():
    print(f'{k} é igual a {v}.')
