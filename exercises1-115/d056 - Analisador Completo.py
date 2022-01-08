s_idade = 0
qtd_mulheres = 0
mais_velho = ''
nome_velho = ''

for c in range(1, 5):
    nome = str(input(f'Nome da {c}° Pessoa: ')).strip()
    idade = int(input(f'Idade da {c}° Pessoa: '))
    sexo = int(input(f'[1] Masculino\n[2] Feminino \nDigite o sexo da {c}° Pessoa: '))
    s_idade = s_idade + idade
    if sexo == 1:
        if c == 1:
            mais_velho = idade
            nome_velho = nome
        else:
            if idade > mais_velho:
                mais_velho = idade
                nome_velho = nome
    if sexo == 2:
        if idade < 20:
            qtd_mulheres += 1
media = s_idade / c

print(f'\nMédia de idade: {media:.2f}. \nNome do mais velho: {nome_velho}. \nQuantidade de mulheres de menos de 20 anos: {qtd_mulheres}.')