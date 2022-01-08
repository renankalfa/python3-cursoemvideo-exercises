n = str(input('Insira seu nome completo: ')).strip()
print(f'Seu nome completo é: {n}.')

#Lista
lista = n.split()

#Primeiro Nome
first = lista[0]
print(f'Seu primeiro nome é {first}.')

#Último Nome
last_element = len(lista)
number = int(last_element)
print(f'Seu último nome é {lista[len(lista)-1]}.')

