count = 0
while True:
    tabuada = int(input('Você quer a tabuada de qual número? '))
    if tabuada < 0:
        break
    else:
        print('=' * 4, f'Tabuada do {tabuada}', '=' * 4)
        for c in range (1, 11):
            count = count + 1
            resultado = tabuada * count
            print(f'{tabuada} x {count} = {resultado}')
print('Programa TABUADA encerrado. Volte sempre!')