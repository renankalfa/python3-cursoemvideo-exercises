from time import sleep

print('*=' * 2, 'Estouro de fogos!', '*=' * 2)

for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\033[31mBooom!!')
