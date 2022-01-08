def aumentar(n=0, a=0, format=True):
    m = n * (1 + a/100)
    if format is True:
        return moeda(m)
    else:
        return m


def diminuir(n=0, d=0, format=True):
    m = n * (1 - d/100)
    if format is True:
        return moeda(m)
    else:
        return m


def dobro(n=0, format=True):
    m = n * 2
    if format is True:
        return moeda(m)
    else:
        return m


def metade(n=0, format=True):
    m = n / 2
    if format is True:
        return moeda(m)
    else:
        return m


def moeda(n=0):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(p=0,a=50,r=50):
    print('=' * 30)
    print(f'{"Tabela de Valores":^30}')
    print('=' * 30)
    print(f'Preço analisado: \t{moeda(p):>10}')
    print(f'Dobro do preço: \t{dobro(p):>10}')
    print(f'Metade do preço: \t{metade(p):>10}')
    print(f'Aumento de {a}%: \t{aumentar(p, a):>10}')
    print(f'Redução de {r}%: \t{diminuir(p, r):>10}')
    print('=' * 30)
