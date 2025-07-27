"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""
import random
import time
computador = random.randint(0,5) # faz o computador "PENSAR!"
print('-=-' * 20)
print('       Vou pensa em um Numero de 0 A 5 !')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei ?:')) # jogar digita um numero !
print('Analizando . . .')
time.sleep(3)  #espera 3 segundo para aparece a mensagem if
if computador == jogador:
    print(f'Parabens Você ganhou!')
else:
    print(f'Você errou !, o Numero que eu Pensei é {computador} e nao {jogador}')
