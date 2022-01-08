nome = str(input('Insira seu nome completo: ')).strip()
print(f'Em maiúsculo: {nome.upper()}')
print(f'Em minúsculo: {nome.lower()}')

#Número de letras - número de espaços
nospace = len(nome) - nome.count(' ')
print(f'Número de letras: {nospace}')

#Trasnformar em lista e contar o número do primeiro elemento
lista = nome.split()
print(f'Número de letras no primeiro nome: {len(lista[0])}')