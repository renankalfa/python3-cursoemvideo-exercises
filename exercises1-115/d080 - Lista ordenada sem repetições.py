lista = []
for c in range(5):
    n1 = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n1)
        print(f'{n1} primeiro adicionado à lista.')
    else:
        if n1 > max(lista):
            lista.append(n1)
            print(f'{n1} foi adicionado no final da lista.')
        elif n1 < min(lista):
            lista.insert(0, n1)
            print(f'{n1} foi adicionado no início da lista')
        else:
            for pos, ct in enumerate(lista):
                if ct > n1:
                    lista.insert(pos, n1)
                    print(f'Adicionado na posição {pos} da lista.')
                    break
print('=*' * 22)
print(f'Os valores digitados foram {lista}')