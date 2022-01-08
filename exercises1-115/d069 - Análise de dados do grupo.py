cp_18 = c_h = c_m20 = 0
count = 1

while True:
    idade = int(input(f'Qual a sua idade ({count}° Pessoa)? '))
    sexo = str(input(f'Qual o seu sexo [M/F]? ')).upper()
    count += 1
    if idade > 18:
        cp_18 += 1
    if sexo == 'M':
        c_h += 1
    if sexo == 'F':
        if idade < 20:
            c_m20 += 1
    pergunta = str(input('Você quer continuar [S/N]: ')).upper()
    if pergunta == 'N':
        break

print(f'Relatório final: \na) Pessoas com mais de 18 anos: {cp_18}. \nb) Homens cadastrados: {c_h}'
      f'\nc) Mulhes com menos de 20 anos: {c_m20}.')
