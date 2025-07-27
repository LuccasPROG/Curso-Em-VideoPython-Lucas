"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 10
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""
from time import sleep
from random import randint
v = 0
while True:
    computador = randint(1,10)
    print('-=-' * 10)
    print('     Jogo da Adiviação!')
    print('-=-' * 10)
    print('Pensei em um Numero de 1 a 10.')
    jogador = int(input('Palpite:'))
    print('Carregando', end='')
    print('.', end='', flush=(True))
    sleep(1)
    print('.',end='', flush=(True))
    sleep(1)
    print('.', flush=(True))
    sleep(2)
    if jogador == computador:
        v += 1
        print('-=-' * 10)
        print(f'Você ja venceu {v} veses consecutivas')
    else:
        print('-=-' * 10)
        print(f'Você Perdeu! eu Pensei no Numero {computador}')
    opçao = ' '
    while opçao not in 'S/N':
        print('-=-' * 10)
        opçao = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
        print('-=-' * 10)
    if opçao == 'N':
        break
print('=-'* 8)
print('    JOGOS')
print('=-' * 8)
print(f'Game Over. Você ganhou {v} vezes consecutivas')