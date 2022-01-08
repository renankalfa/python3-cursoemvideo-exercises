from d115.tratamento import testanome, testaidade
from d115.visuais import formatar
from time import sleep
info = {'renan barbosa': 20, 'Kalfa dos Santos': 30}


def armazenar(nome='', anos=0):
    sleep(0.5)
    formatar('Novo Cadastro')
    sleep(0.5)
    nome = testanome(input('Digite o seu nome: '))
    anos = testaidade('Digite a sua idade: ')
    info[f'{nome}'] = anos


def mostrarcadastradas():
    sleep(0.5)
    formatar('PESSOAS CADASTRADAS')
    for keys, values in info.items():
        sleep(0.5)
        print(f'{keys.title():.<33}{values} anos')
    sleep(0.5)
    print('=' * 40)
    sleep(2)
