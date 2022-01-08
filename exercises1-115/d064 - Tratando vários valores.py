print('=*' * 1, 'Tente a sorte', '=*' * 1)
n1 = int(input('Tente a sorte: '))
count = 1
soma = n1

while n1 != 999:
    count += 1
    n1 = int(input(f'Tente a sorte pela {count}° vez: '))
    if n1 != 999:
        soma += n1

print(f'Foram necessárias {count} tentativas/números digitados e a soma deu {soma}.')