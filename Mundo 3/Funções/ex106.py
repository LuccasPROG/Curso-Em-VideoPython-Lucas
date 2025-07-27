"""Faça um programa que tenha uma função chamada area(), que receba dimensões
 de um terreno retangular (largura e comprimento) e mostre a área do terreno
"""
def area(larg, conp):
    total = larg * conp
    print(f'A Area do seu terreno {larg}x{conp} é a de {total}m²')

#Inicio...
print('-='*15)
print('Terrenos Lucas III')
print('-='*15)
l = float(input('Digite sua Largura(m):'))
c = float(input('Digite sua Altura(m):'))
area(l,c)