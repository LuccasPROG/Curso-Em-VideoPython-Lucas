import moeda
p = float(input('Digite um preço R$'))
print(f'A metade do {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro do {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% fica {moeda.moeda(moeda.aumento(p, 10))}')
print(f'Descontando 10% fica {moeda.moeda(moeda.diminuir(p,10))}')
