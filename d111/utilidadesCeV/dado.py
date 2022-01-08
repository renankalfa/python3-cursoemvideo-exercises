def testmoneydigit(n='Preço: '):
    while True:
        valor = input(n)
        if valor.replace('.', '').replace(',', '').isdigit() and valor.count('.') < 2 and valor.count(',') < 2:
            return float(valor.replace(',', '.'))
        print(f'ERRO: "{valor}" é um preço inválido!')
