"""Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
"""

v = int(input('Digite a Velocidade Do Seu Carro :'))
if v >= 80:
        print('Você foi Multado Por Ultrapassar 80 KM/H')
        multa = (v - 80) * 7
        print(f'Você tera que pagar R${multa}')
print('Tenha um Bom Dia! Dirija com segurança!.')
