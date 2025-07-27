'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''


import datetime
atual = datetime.date.today().year
nasc = int(input('Digite sua data de nascimento:'))
idade = atual - nasc
if idade <= 9:
    print(f'Você ja tem {idade} anos, e é um Nadador MIRIM')
elif idade <= 14:
    print(f'Você ja tem {idade} anos, e é um Nadador Infantil')
elif idade <= 19:
    print(f'Você ja tem {idade} anos, e é um Nadador Junior')
elif idade <= 25:
    print(f'Você ja tem {idade} anos, e é um Nadador Sênior')
else:
    print(f'Você ja tem {idade} anos, e é um Nadador MASTER!!!')