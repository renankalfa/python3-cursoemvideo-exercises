first_term = int(input('Primeiro Termo: '))
razao = int(input('Razão da P.A.: '))
cont = 0

for c in range (0, 10):
    cont = cont + 1
    an = first_term + razao * (cont -1)
    print(f'Termo a{cont}= {an}')
