''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.'''
from random import randint
v = 0
while True:
    computador = randint(1, 10)
    print('=-' * 15)
    print('  VAMOS JOGAR IMPAR OU PAR:')
    print('=-' * 15)
    jogador = int(input('Digite um Valor:'))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Impar ou Par [I/P]:')).upper().strip()[0]
    soma = jogador + computador
    if jogador % 2 == 0:
        iop = 'PAR'
    else:
        iop = 'IMPAR'
    print('=-'*15)
    print(f'Você jogou {jogador} e Computador jogou {computador}, Total de {soma} é {iop}')
    print('=-' *15)
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu !')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print(f'Vamos Jogar Novamente, Você ja venceu {v} Vezes!')
print(f'Game Over! Você venceu {v} Vezes.')