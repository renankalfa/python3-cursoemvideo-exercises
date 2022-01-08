f = str(input('Insira uma frase qualquer: ')).strip()

# Quantas vezes aparece a letra "A"

a = f.lower().count('a')
print(f'Número de letras a: {a}')

#Posições que aparecem

first = f.lower().find('a') + 1
last = f.lower().rfind('a') + 1

print(f'Posição que aparece primeiro: {first} \nPosição que aparece por último: {last}')