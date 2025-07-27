#digite um script que leia um nome e fale o primeiro nome digitado e o ultimo nome digitado



nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Muito Prazer !')
print(f'Seu  Primeiro Nome é {n[0]}')
print(f'Seu Ultimo Nome é {n[len(n)-1]}')
