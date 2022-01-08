maior = 0
menor = 0

for c in range(1,6):
    pesos = float(input(f'Peso da {c}° Pessoa: '))
    if c == 1:
        menor = pesos
        maior = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos

print(f'Maior peso: {maior} \nMenor peso: {menor}')