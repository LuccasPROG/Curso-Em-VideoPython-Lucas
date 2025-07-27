'''
Melhore o exercício 67, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
'''

print('Gerador de PA') #mesmo exercicio usado no 56 feito por outra estrutura enquanto ! while
print('=-=' * 20)
primeiro = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))
termo = primeiro #termo passa a setorna o primeiro termo
cont = 1
mais = 10 #vai começa
começo = 0
while mais != 0: # enquanto mais difirente de 0 faça
    começo = começo + mais # i começo vai receber a variavel mais que vai ser quantos eu quero fazer ainda!
    while cont <= começo: #vai escrever o começo 
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos Termos Deseja a Mais:')) #pergunta quantos deseja mais
print(f'O Total de Termos Digitados é {começo} ') #fala o total de numeros digitados!
print('Encerrado!') #Encerra