from lib.interface import *

def ArquivoExiste(nome): # verifica se existe um arquivo!
    try:
        a = open(nome, 'rt') # le um arquivo!
        a.close() # fecha um arquivo
    except FileNotFoundError: # fala se tem ou não um arquivo
        return False
    else:
        return True
    

def criararquivo(nome): # cria um arquivo !
    try: 
        a = open(nome, 'wt+')# wt+ cria um arquivo !
        a.close() # um arquivo fecha
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome): # ler o arquivo!
    try:
        a = open(nome, 'rt') # le um arquivo
    except:
        print('Erro ao ler o arquivo!') # error por qualquer que lia
    else:
        cabeçalho('PESSOAS CADASTRADAS') # cabeçalho
        for linha in a:
            dado = linha.strip().split(';')
            idade = dado[1].strip()
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastra(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq,'at') # abre um arquivo!
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome} ; {idade}\n') # write add algo no arquivo
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()