# crie um script que digita um numero  e separa o numero digitado em unidade dezena centena milhar
from time import sleep
#  forma mais facil e funciona tudo !
num = int(input('Digite Seu Numero:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando', end='')
sleep(1)
print('.', end='', flush=(True))
sleep(1)
print('.', end='', flush=(True))
sleep(1)
print('.', flush=(True))
sleep(1)
print('-=-' * 8)
print(f'Unidade : {u}')
print(f'Dezena : {d}')
print(f'Centena : {c}')
print(f'Milhar : {m}')
print('-=-' * 8)

'''num = int(input('Digite Seu Numero:'))
n = str(num)
print('Analizando ...')
print(f'Unidade : {n[3]}')
print(f'Dezena : {n[2]}')
print(f'Centena : {n[1]}')
print(f'Milhar : {n[0]}')''' #- uma forma de fazer mais nao total nao conta so dezenas ou somente unidades !