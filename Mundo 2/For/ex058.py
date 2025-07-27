''' Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços'''
# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona

frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
'''inverso = junto[::-1]''' #forma sem a laço de repetição!
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'o Inverso de {frase} é {inverso}')
if inverso == junto:
    print('Temos um Políndromo')
else:
    print('Não Temos um Políndromo!!')