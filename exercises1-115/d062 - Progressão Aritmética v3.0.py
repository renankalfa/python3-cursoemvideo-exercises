first = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A: '))
count = 0

while count < 10:
    count += 1
    term = first + razao * (count - 1)
    print(f'a{count} = {term}')

amais = int(input('Quantos termos a mais você irá querer ver? '))
count2 = 0

while amais > 0:
    if count2 < amais:
        count += 1
        count2 += 1
        term = first + razao * (count - 1)
        print(f'a{count} = {term}')
    else:
        count2 = 0
        amais = int(input('Quantos termos a mais você irá querer ver? '))

print('Programa encerrado!')
