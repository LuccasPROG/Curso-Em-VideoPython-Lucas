"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem

Seu programa tem que realizar três contagens através da função criada

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada

--> print(f"{valor} ", end="")  # Exemplo de print espaçado
"""
from time import sleep

def linha():
    print('-=' * 20)

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
    print('Fim!', flush=True)
    print()  # quebra de linha que resolve o bug visual

# Programa principal
contador(1, 10, 1)
contador(10, 1, 2)
linha()
print('Agora é Sua Vez:')
while True:
    ini = int(input('Inicio:   '))
    final = int(input('Final:   '))
    passo = int(input('Passo:    '))
    contador(ini, final, passo)
    resp = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('Agradeço por usar o contador!')