from d115.visuais import *


def arquivoExiste(nome='novoarquivo.txt'):
    try:
        a = open(nome, 'rt', encoding='utf-8')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome='novoarquivo.txt'):
    try:
        a = open(nome, 'wt', encoding='utf-8')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome='novoarquivo.txt'):
    from time import sleep
    try:
        a = open(nome, 'rt', encoding='utf-8')
    except:
        print('Erro ao ler o arquivo!')
    else:
        sleep(0.5)
        formatar('pessoas cadastradas')
        for linha in a:
            dado = linha.replace('\n', '').split(';')
            sleep(0.3)
            print(f'{dado[0]:<33}{dado[1]} anos')
        a.close()
        print('=' * 40)
        sleep(2)


def armazenarArquivo(nome='novoarquivo.txt', nomep='', idade=0):
    try:
        a = open(nome, 'r', encoding='utf-8')
        conteudo = a.readlines()
        conteudo.append(f'{nomep};{str(idade)}\n')
    except Exception as erro:
        print('Erro de gravação!')
        print(erro)
    else:
        a = open(nome, 'wt', encoding='utf-8')
        a.writelines(conteudo)
        a.close()
