# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere R$ 3.27 = US$ 1

n = float(input("Quanto dinheiro você tem? \nR$"))
dolar = 3.27
conversao = n / dolar
print("Com R${} você pode comprar US$ {:.2f}.".format(n, conversao))
n1 = float(input('Digite uma Nota:'))
n2 = float(input('Digite outra Nota:'))
m = (n1 + n2) / 2
print(f'A medias das notas cadastrada é : {m}')