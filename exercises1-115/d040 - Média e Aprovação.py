nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2)/2

if media < 5:
    print('REPROVADO!')
elif 5 <= media < 6.9:
    print('RECUPERAÇÃO JÁ!')
else:
    print('APROVADO!')