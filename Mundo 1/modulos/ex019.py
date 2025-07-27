#Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) 
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.


import math
co = float(input('Digite um Valor para o Cateto oposto: '))
ca = float(input('Digite um valor para o Cateto adiacente: '))
hp = math.hypot(co, ca)
print(f'A Hipotenusa Vale {hp:.2f}')  # forma usando a biblioteca math hehehe