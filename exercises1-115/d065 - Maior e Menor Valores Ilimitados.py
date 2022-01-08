n = int(input('Digite um número: '))
count = 1
sn = str(input('Você quer continuar (S/N)? ')).upper()
st = maior = menor = n

while sn == 'S':
    count += 1
    n1 = int(input('Digite um número: '))
    sn = str(input('Você quer continuar (S/N)? ')).upper()
    st += n1
    if n1 > n:
        maior = n1
    if n1 < n:
        menor = n1
    n = n1
media = st / count
print(f'Soma = {st}, Números = {count}, Maior = {maior}, Menor = {menor}, Média = {media:.2f}')