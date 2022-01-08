count = soma = 0
while True:
    n1 = int(input('Digite um número (999 para parar): '))
    if n1 == 999:
        break
    count += 1
    soma += n1
print(f'A soma dos {count} números foi {soma}!')