from random import shuffle

aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))
alunos = [aluno4, aluno3, aluno2, aluno1]
print(alunos)

shuffle(alunos)

print(alunos)