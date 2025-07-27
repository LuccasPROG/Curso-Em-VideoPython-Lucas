''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''
from time import sleep
num = int(input('Digite um Numero Inteiro:'))
print('''Escolha um Numero Das Opção Abaixo:
[1] Converter Para BINARIO
[2] Converter Para OCTAL
[3] Converter Para HEXADECIMAL''')
opção = int(input('Sua Opção:'))
print(f'Analizando . . .')
sleep(2)
if opção == 1:
    print(f'O Valor {num} Convertido Para Binario é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'O Valor {num} Convertido Para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'O Valor {num} Convertido Para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção Invalida, Tente Novamente!')