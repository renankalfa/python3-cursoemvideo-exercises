frase = str(input('Insira a frase: '))
separada = frase.upper().split()
unica = ''.join(separada)
inverso = ''

for c in range(len(unica) -1, -1, -1):
    inverso = inverso + unica[c]
print(unica, inverso)
if unica == inverso:
    print('É palíndromo!')
else:
    print('Não é palíndromo.')