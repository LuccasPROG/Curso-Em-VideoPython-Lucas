# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado


d = int(input('Digite Quantos dias Passou com veiculo(Alugado):'))
km = float(input('Digite Quantos KM você rodou no veiculo:'))
dp = d * 60  #calcula os dias
kmp = km * 0.15 #calcula os KM
total = dp + kmp #Calcula o TOTAL
print(f'Você passou {d} e Tera que Pagar R${total:.2f}')