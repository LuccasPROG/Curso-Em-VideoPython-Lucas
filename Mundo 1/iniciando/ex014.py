# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento


nome = input('Digite seu Nome:')
salario = int(input('Qual o Valor do Salario do Funcionario R$\033[32m'))
desconto = salario + (salario * 15 / 100)
print(f'\033[m o {nome} teve seu salario com 15% de desconto seria R$\033[32m{desconto:.2f}\033[m')
print(f'Salario do {nome} antes do desconto era R$\033[32m{salario:.2f}\033[m')