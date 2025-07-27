#crie um script que digite alguma frase e mostre a primeira letra a que aparece a posição
#a ultima letra e posição






frase = str(input('Digite Alguma Frase :')).strip().upper()
print(f'A Letra A Aparece na Frase : {frase.count('A')}')
print(f'A Primeira Letra A apareceu na Posição : {frase.find('A') + 1}')
print(f'A Ultima Letra A apareceu na posição : {frase.rfind('A') + 1}')