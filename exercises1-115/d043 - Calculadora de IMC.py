peso = float(input('Seu peso (kg): '))
altura = float(input('Sua altura (m): '))

imc = peso / (altura ** 2)

if 0 < imc < 18.5:
    print(f'\033[31mSeu IMC é {imc:.2f} e você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print(f'\033[32mSeu IMC é {imc:.2f} e você está no PESO IDEIAL!')
elif 25 <= imc < 30:
    print(f'\033[33mSeu IMC é {imc:.2f} e você está com SOBREPRESO!')
elif 30 <= imc < 40:
    print(f'\033[35mSeu IMC é {imc:.2f} e você está com OBESIDADE!')
elif imc >= 40:
    print(f'\033[31mSeu IMC é {imc:.2f} e você está com OBESIDADE MÓRBIDA!')
else:
    print('Dados incorretos.')