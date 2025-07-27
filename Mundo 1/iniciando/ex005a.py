#Crie um Script 
n1 = int(input('Digite um Numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
sub = n1 - n2
d = n1 / n2
di = n1 // n2
m = n1*n2
p = n1 ** n2
print(f'A soma :{s}, a subtração :{sub}, divição :{d:.3f}', end=" >>> ")
print(f'Divisão inteira :{di}, Multiplicação :{m}, potencia :{p}')
