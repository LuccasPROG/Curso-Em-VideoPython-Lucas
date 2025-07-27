import moeda
p = float(input('Digite um preço R$'))
print(f'A metade do {moeda.moeda(p)} é {(moeda.metade(p,formato=True))}')
print(f'O dobro do {moeda.moeda(p)} é {(moeda.dobro(p,formato=True))}')
print(f'Aumentando 10% fica {(moeda.aumento(p, 10,formato=True))}')
print(f'Descontando 10% fica {moeda.diminuir(p,10,formato=True)}')
