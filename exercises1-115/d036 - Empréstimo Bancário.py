valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário: R$ '))
anos = float(input('Em quantos anos deseja pagar: '))

#Contas

meses = anos * 12
prestacao = valor_casa / meses
# prestacao = valor_casa / (anos * 12)
trinta_salario = 0.3 * salario

#Condições

if prestacao > trinta_salario:
    print(f'Empréstimo negado! A prestação seria de R$ {prestacao:.2f}')
else:
    print(f'Empréstimo aceito! \nPrestação mensal: R$ {prestacao:.2f}')