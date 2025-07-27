"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
"""


distancia = float(input('Digite a Distancia da sua viagem (KM):'))
print(f'Você esta prestes a fazer uma viagem de {distancia}')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'Você ira percorrer {distancia} e tera que pagar {preco:.2f}')