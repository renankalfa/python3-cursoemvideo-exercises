number = int(input('Digite o número: '))
numero = number
antecessor = numero - 1

while antecessor != 1:
    numero = numero * antecessor
    antecessor = antecessor - 1

print(f'O fatorial de {number} é {numero}.')
