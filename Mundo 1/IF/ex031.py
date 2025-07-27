#crie um script que digita dois numeros e faz a medida nas notas digitadas!
n1 = float(input('Digite um Numero:'))
n2 = float(input('Digite Outro Numero:'))
m = (n1 + n2)/2  # faz a media das notas digitadas
print(f'Sua Media Foi de :{m:.1f}')
if m >= 6.0:
    print('Parabens, Boa Nota!')
else:
    print('Nota Baixa, Estude Mais!!!')