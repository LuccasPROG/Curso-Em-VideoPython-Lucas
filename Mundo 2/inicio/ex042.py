'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''
n1 = int(input('Primeiro Numero:'))
n2 = int(input('Segundo Numero:'))
if n1 > n2:
    print(f'O Primeiro Numero é Maior')
elif n2 > n1:
    print('O Segundo Numero é Maior')
elif n1 == n2:
    print('Os Dois numeros São Igual!')
    