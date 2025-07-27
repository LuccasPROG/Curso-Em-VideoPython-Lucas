"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
choices_list = ["pedra", "papel", "tesoura"]
print("""
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
""")
from random import randint
from time import sleep
itens = ('Pedra', "Papel", "Tesoura")
computador = randint(0, 2)
print('-=-' * 14)
print('     JOGO: PEDRA PAPEL OU TESOURA !')
print('-=-' * 14)
print('''Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Faça Sua Jogada! :'))
print('-=-' * 12)
print(f'Computador Jogou {itens[computador]}')
print(f'Jogador Jogou {itens[jogador]}')
print('-=-' * 12)
print('Jo')
sleep (1)
print('Ken')
sleep (1)
print('PO !!')
sleep (1)
print('-=-' * 12)
if  computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Computador Venceu!')
    else:
        print(f'Jogada Invalida, Tente Novamente!')
elif computador == 1: #Computador Jogou PAPEL
    if jogador == 0:
        print('Computador Vence!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador Venceu!')
    else:
        print(f'Jogada Invalida, Tente Novamente!')
elif computador == 2: # Computador Jogou Tesoura
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Computador Venceu!')
    elif jogador == 2:
        print(('EMPATE!!'))
    else:
        print(f'Jogada Invalida, Tente Novamente!')
print('-=-' * 12)