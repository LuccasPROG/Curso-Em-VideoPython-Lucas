#crie um script que leia um nome e coloque ele em maiusc minusc conta letras etc...

import time
nome = str(input('Digite seu Nome completo :')).strip()
print('Analisando seu Nome ...')
time.sleep(2)
print(f'Seu Nome em Maiusculo é: {nome.upper()}')
print(f'Seu Nome em minusculo é: {nome.lower()}')
print(f'Seu Nome ao Todo tem {len(nome) - nome.count(' ')} Letras !') #conta quantas letras tem fora os espaços
separa = nome.split() #separar os nomes para poder escolher!
print(f'Seu Primeiro Nome é {separa[0]} e ele tem {len(separa[0])} Letras')