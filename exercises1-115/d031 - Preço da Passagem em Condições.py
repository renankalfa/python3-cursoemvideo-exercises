dist = float(input('Distância da viagem (Km): '))
print(f'Distância da viagem: {dist:.2f} Km')

if dist <= 200:
    p1 = dist * 0.50
    print(f'O preço da passagem: R${p1:.2f}')
else:
    p2 = dist * 0.45
    print(f'O preço da passagem foi de {p2:.2f} reais.')