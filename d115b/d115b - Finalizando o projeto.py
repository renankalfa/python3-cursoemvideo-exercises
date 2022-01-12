from d115.tratamento import *
from d115.bancodedados import *
from d115b.arquivos import *

arq = 'dados.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    menu('Mostrar Pessoas cadastradas', 'Cadastrar Pessoa', 'Encerrar Programa')
    option = testaoption(input('\033[33mSua opção: \033[m'))
    if option == 1:
        lerArquivo(arq)
    if option == 2:
        from time import sleep
        sleep(0.5)
        formatar('cadastro de pessoa')
        nome = testanome('Digite o seu nome: ')
        idade = testaidade('Digite a sua idade: ')
        armazenarArquivo(arq, nome, idade)
    if option == 3:
        encerrar()
        break
