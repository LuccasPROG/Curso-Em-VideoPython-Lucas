''' Melhore o jogo de onde o computador vai "pensar"
em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer
'''
from random import randint
computador = randint(1,10)
print('-=' * 20)
print('        Jogo do Adivinhe !')
print('-=' * 20)
print('Pensei em um Numero de 1 a 10, Tente Adivinhar!')
jogador = int(input('Seu Palpite: '))
cont = 1
while jogador != computador:
    if computador < jogador:
        print('Menos, Tente mais uma vez . .')
    elif computador > jogador:
        print('Mais, Tente mais uma vez . .')
    jogador = int(input('Seu Palpite:'))
    cont = cont + 1

print(f'Acertou com {cont} Tentativas, Parabens!')