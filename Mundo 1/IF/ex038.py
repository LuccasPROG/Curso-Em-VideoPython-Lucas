"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de R$ 15%.
"""

salario = float(input('Digite o Salario do Funcionario R$'))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print(f'Quem Ganhava R$\033[32m{salario:.2f}\033[m Passa a Ganhar R$\033[32m{aumento:.2f}\033[m')