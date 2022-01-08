def testanome(phrase=''):
    while True:
        name = input(phrase)
        list_words = name.split()
        c = 0
        for word in list_words:
            if word.isalpha() is False:
                print('\033[31mErro! Digite um nome válido!\033[m')
                c += 1
        if c == 0:
            break
    return ' '.join(list_words)


# Conseguir com acento /\ #


def testaidade(frase):
    while True:
        idade = input(frase)
        if idade.isdecimal() and 0 <= int(idade) < 120:
            return int(idade)
        print('\033[31mErro! Digite um número inteiro válido!\033[m')


def testaoption(n):
    while n not in '123':
        print('\033[31mErro! Digite um opção válida!')
        n = input('\033[33mSua opção: \033[m')
    return int(n)
