first= int(input('Primeiro termo da P.A: '))
razao = int(input('Razão da P.A: '))
count = 0

while count < 10:
    count += 1
    term = first + razao * (count - 1)
    print(f'a{count} = {term}')

