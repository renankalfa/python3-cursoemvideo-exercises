palavras = ('aprender', 'programar', 'linguaguem', 'python',
            'curso', 'gratis')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for silaba in palavra:
        if silaba in vogais:
            print(silaba, end=' ')
