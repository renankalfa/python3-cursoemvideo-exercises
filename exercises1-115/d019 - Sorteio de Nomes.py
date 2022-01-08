from random import choice

aluno1 = str(input('Nome de um aluno: '))
aluno2 = str(input('Nome de outro aluno: '))
aluno3 = str(input('Nome de outro aluno: '))
aluno4 = str(input('Nome do último aluno: '))
alunos = [aluno4, aluno3, aluno2, aluno1]

result = choice(alunos)

print(f'O aluno sorteado foi o(a) {result}.')