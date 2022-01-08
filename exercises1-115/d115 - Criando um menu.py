from d115.visuais import *
from d115.tratamento import *
from d115.bancodedados import *

while True:
    menu('Pessoas cadastradas', 'Cadastrar Pessoa', 'Encerrar Programa')
    option = testaoption(input('\033[33mSua opção: \033[m'))
    if option == 1:
        mostrarcadastradas()
    if option == 2:
        armazenar()
    if option == 3:
        encerrar()
        break
