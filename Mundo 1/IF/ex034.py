"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""


from time import sleep
print('-=-' * 10)
print('    Jogo do Impar Ou Par')
print('-=-' * 10)
iop = int(input('Digite um Numero:')) # fala para digitar um numero !
print('Analizando', end='')
sleep(2) # espera 2 segundos
print('.',end='',flush=(True))
sleep(2)
print('.', flush=(True))
sleep(2)
if iop % 2 == 0: # faz o calculo para saber se é impar ou par !
    print(f'O Numero {iop} é Par!')
else:
    print(f'O Numero {iop} é Impar!')