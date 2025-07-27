"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Obs.: aposentadoria em 35 anos de contribuição.
"""
from datetime import datetime
from time import sleep
info = dict()
info['nome'] = str(input('Digite seu Nome:'))
ano = int(input('Digite seu Ano de Nascimento:'))
info['idade'] = (datetime.now().year  - ano)
info['ctps'] = int(input('Digite sua Carteira de Trabalho (0 Caso não Tiver!) :'))
if info['ctps'] != 0:
    info['contratação'] = int(input('Ano da Contratação:'))
    info['salario'] = int(input('Salario R$:'))
    info['aposentadoria'] = info['idade'] + ((info['contratação'] + 35) - datetime.now().year)
print('-=' * 15)
print('           Dados')
print('-='*15)
for k, v in info.items():
    print(f'  - {k} Tem o valor :{v}')
    sleep(1)
print('-=' * 15)
print()
