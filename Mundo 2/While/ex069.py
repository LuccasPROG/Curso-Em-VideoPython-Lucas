'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)

'''
print ('=-' * 30)
print('Sequencia de Fibonacci')
print('=-' * 30)
n = int(input('Quantos termos você quer mostrar ?'))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
cont = 3 
while cont <= n:
    t3 = t1 + t2
    print(F'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')