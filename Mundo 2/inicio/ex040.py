'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''
casa = float(input('Qual o Valor da Casa:'))
salario = float(input('Qual o Valor do Seu Salario Mensal:'))
anos = int(input('Em quantos anos de financeamento:'))
fin = casa / (anos * 12) #faz o calculo do financeamento
minimo = (salario * 30) / 100 #calcula o minimo que podera compra 30%
print(f'Para pagar uma casa no valor de {casa:.2f} em {anos}anos a prestação ficara de R${fin:.2f}')
if fin <=  minimo:
    print('Você pode Realizar o Financeamento!')
else:
    print('Você nao podera Realizar o Financeamento!')