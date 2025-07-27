# crie um script que leia um numero e converta esse dinheiro em doelar ou euro
r = float(input('Digite Quantos Dinheiro Você tem R$:'))
d = r / 5.46 #Soma o Dolar!
e = r / 6.45 # soma o Euro!
print('-=-' * 20)
print('-=-' * 20)
print('Conversor de Moedas')
print(f'Você tem R${r:.2f} em Reais e podera troca em dolares por US$:{d:.2f}')
print(f'Você tem R${r:.2f} em Reais e Podera troca em Euro por €{e:.2f}')
print('-=-' * 70)