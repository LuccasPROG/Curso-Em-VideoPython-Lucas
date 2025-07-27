"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.

Faça também um programa que importe esse módulo e use algumas dessas funções.

Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula.

o 'diminuir()', mesma coisa.

"""
import moeda
p = float(input('Digite um preço R$'))
print(f'A metade do {p:.2f} é {moeda.metade(p):.2f}')
print(f'O dobro do {p:.2f} é {moeda.dobro(p):.2f}')
print(f'Aumentando 10% fica {moeda.aumento(p, 10):.2f}')
print(f'Descontando 10% fica {moeda.diminuir(p,10):.2f}')
