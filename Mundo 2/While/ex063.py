'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''
sexo = str(input('Informe Seu Sexo [M/F]:')).strip().upper()[0]                     
while sexo not in 'MF': # enquanto sexo nao tiver M OU F repita a mensagem abaixo!
    sexo = str(input('Dados Invalido, Por favor Informe Seu Sexo [M/F]:')).strip().upper()[0]
print(f'O Sexo {sexo} Registrado com Sucesso!')