''' Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''

from time import sleep
while True:
    print('=-' * 20)
    n = int(input('Digite um Numero Para Sua Taboada:'))
    print('=-' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        s = n * c
        print(f'{n} x {c} = {s}')
    print('')
print('Encerrando', end='')
sleep(1)
print('.',end='',flush=(True))
sleep(1)
print('.',end='',flush=(True)) #faz com que o . seja impresso imediatamente sem atraso!!!
sleep(1)
print('.',flush=(True))
sleep(1)
print('Programa De Tabuada Encerrado, Volte Sempre')