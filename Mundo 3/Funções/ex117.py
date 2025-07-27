"""
Faça um minissistema que utilize o interactive help do Python

O usuário vai digitar o comando e o manual vai aparecer.

Quando o usuário digitar a palavra "FIM", o programa se encerrará!.

OBS: use cores.
"""
from time import sleep # chama a biblioteca sleep
cores = ('\033[m',#nada 0   # cores diferentes
         '\033[0;30;41m',#vermelho 1 
         '\033[0;30;42m',#verde 2 
         '\033[0;30;44m',#azul 3 
         '\033[7;30m');#branco 4
def ajuda(a): # chama o comando help 
    titulo(f'Acessando o manual do comando \'{a}\'',3)
    print(cores[4], end='')
    help(a)
    print(cores[0], end='')
    sleep(2)
def titulo(msg, cor=0): #faz um titulo de acordo com o texto digitado!
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print(cores[0], end='')
    print('~' * tam)
    sleep(1)

#Inicio:
comando = ''
while True: # realiza o loop ate . . .
    titulo('SISTEMA DE AJUDA PyHELP', 3) # chama a função titulo
    comando = str(input('Função ou Biblioteca >')) #pergunta qual função quer ver!
    if comando.upper() == 'FIM': # sair do pograma
        break
    else:
        ajuda(comando) #chama a função ajuda
titulo('Até Logo!', 1) # chama a função titulo