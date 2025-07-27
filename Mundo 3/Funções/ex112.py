"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""
from time import sleep
def voto(ano):
    from datetime import datetime
    idade =  datetime.now().year - ano
    return idade
#Inicio:
print('-=' * 15)
print('       Analize de Voto')
print('-='*15)
while True:
    v = int(input('Digite seu ano de nascimento:'))
    print('Analizando', end='')
    print('.', end='',flush=True)
    sleep(0.5)
    print('.',end='',flush=True)
    sleep(0.5)
    print('.',flush=True)
    sleep(0.20)
    print('-='*15)
    if voto(v) <= 16:
        print(f'Com {voto(v)} anos, não vota!')
    elif voto(v) >= 18 and voto(v) < 65:
        print(f'Com {voto(v)} anos, é obrigatorio votar!!')
    else:
        print(f'Com {voto(v)} anos, é opicional votar!')
    resp = ' '
    while resp  not in 'SN':
        resp = str(input('Deseja Continuar? [S/N]:')).strip().upper()[0]
        if resp not in 'SN':
            print('Erro! escreva somente com S ou N!')
    if resp == 'N':
        break
print('-='*29)
sleep(1)
print('Encerrando . .')
sleep(1)
print('>> Obrigado Por usar nosso site, volte sempre! <<')