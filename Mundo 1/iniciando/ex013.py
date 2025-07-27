# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto



p = int(input('Digite o Valor do Produto R$'))
md = p * 5 / 100
d = p - md 
print(f'O Valor do Produto Sem Desconto R$\033[32m{p}\033[m')
print(f'O Valor do Produto Com Desconto R$\033[32m{d}\033[m')