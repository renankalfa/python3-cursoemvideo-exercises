def notas(*notas, sit=True):
    """
    -> Recebe as notas e retorna um dicionário com informações
    :param notas: notas de cada aluno (pode-se escrever mais de uma)
    :param sit: True -> mostra a situação geral, False -> não mostra a situação geral
    :return: dicionário com informações como quantidade de nota(s), maior(es) e menor(es) nota(s),
    além de mostrar, caso o usuário queira, a situação geral.
    """
    somat = cont_notas = 0
    inf = dict()
    for nota in notas:
        cont_notas += 1
        somat += nota
    inf['total'] = cont_notas
    inf['maior'] = max(notas)
    inf['menor'] = min(notas)
    inf['média'] = somat / cont_notas
    if sit is True:
        if (somat/ cont_notas) < 5:
            situation = 'RUIM'
        elif 5 <= (somat/ cont_notas) < 7:
            situation = 'MEDIANA'
        else:
            situation = 'ÓTIMA'
        inf['situação'] = situation
    return inf


# Programa Principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)
