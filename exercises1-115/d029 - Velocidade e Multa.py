velocidade = float(input('Velocidade do seu carro (km/h): '))

if velocidade <= 80:
    print('Você se livrou, meu parceiro!')
else:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em R${multa:.2f}!')