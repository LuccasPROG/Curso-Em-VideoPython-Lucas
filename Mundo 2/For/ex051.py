# Faça um programa que mostre na tela
# Uma contagem regressiva para o estouro e fogos de artifício,
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# USANDO LOOP AGORA
from time import sleep
from emoji import emojize
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize('\033[33mBOOOOM \033[m:boom:',language='alias'))