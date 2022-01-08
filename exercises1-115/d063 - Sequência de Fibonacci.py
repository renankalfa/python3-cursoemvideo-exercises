print('=*' * 4, 'Sequência de Fibonacci', '=*' * 4)
n_pri = int(input('Quantos n primeiros termos você quer? '))
count = 2
ant1 = 0
ant2 = 1

if n_pri < 3:
    if n_pri <= 1:
        print('0')
    if n_pri == 2:
        print('0 \n1')
    else:
        print('Número inválido (<0)')
else:
    print('0 \n1')
    while count < n_pri:
        count += 1
        now = ant1 + ant2
        ant1 = ant2
        ant2 = now
        print(now)
print('Programa encerrado')

