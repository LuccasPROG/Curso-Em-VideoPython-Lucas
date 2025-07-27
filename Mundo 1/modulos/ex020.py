# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) 
# e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre
#  o comprimento da hipotenusa.


import math
ag = float(input('Digite o Angulo Desejado :'))
seno = math.sin(math.radians(ag))
cos = math.cos(math.radians(ag))
tan = math.tan(math.radians(ag))
print(f'O Seno : {seno:.2f}')
print(f'O Cosseno: {cos:.2f}')
print(f'A Tangente : {tan:.2f}')