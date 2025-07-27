# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
#  para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²


largura = float(input('Digite uma Largura da parede:'))
alt = float(input('Digite uma Altura da parede:'))
area = largura * alt # Soma a Area!
print(f'Sua parede tem a dimenção de {largura}x{alt} e tem a area de {area}M2')
tinta = area / 2 # soma quantidade de litros nessecairos
print(f'A Quantidade de Tinta nessesaria para pintar a parede é de \033[33m{tinta:.0f}l\033[m de tinta')