'''

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''
import time
peso = float(input('Digite Seu Peso (KG)'))
alt = float(input('Digite Sua Altura (M)'))
imc = peso / (alt ** 2)
print('Analizando . . .')
time.sleep(2)
print(f'Seu IMC é de {imc:.0f} !')
if imc < 18.5:
    print('Classificação:Abaixo do Peso!')
elif imc < 25:
    print(f'Classificação: Peso Ideal!')
elif imc < 30:
    print('Classificação: Sobrepeso!')
elif imc < 40:
    print(f'Classificação Obesidade!')
else:
    print(f'Classificação: Obesidade MÓRBIDA!!!!!')