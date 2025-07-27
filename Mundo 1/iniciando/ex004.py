# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele


nome =  input("Digite Algo: ")
print('o tipo primitivo é :', (type(nome)))         # Mostra o Tipo do primitivo !
print('So tem letras e numeros ? :',(nome.isalnum()))       #Se tem Numeros e Letras!
print('so tem letras ? :', (nome.isalpha()))        # Se tem Letras Somente!
print('So tem numeros ? :', (nome.isnumeric()))      # Se tem Numero somente!
print('todas as letras em MAIUSCULO? :', (nome.isupper()))          # Tudo em Maiusculo !
print('Todas as letras esta em minusculo? :', (nome.islower())) # tudo em minusculo
print('So tem espaçoes? :', (nome.isspace()))        # saber se so tem espaço escrito
print('Esta Captalizada? :', (nome.istitle()))      # saber se esta começa com a letra maiuscula etc . . .