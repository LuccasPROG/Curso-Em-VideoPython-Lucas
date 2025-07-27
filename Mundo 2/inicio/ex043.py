'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''
import datetime
import  time
atual = datetime.date.today().year
nasc = int(input('Digite sua data de nascimento:')) #pergunta a data de nascimento
idade = atual - nasc
print('Analizando . . . ') 
time.sleep(2) #tempo de espera de 2 seconds
print(f'Quem Naceu No Ano de {nasc} tem {idade} anos em {atual}') # informa a idade
if idade == 18: #quem ja tem 18 anos
    print(f'Você ja Pode se Alistar.') 
elif idade < 18: # quem ainda vai fazer 18 anos
    saldo = 18 - idade 
    print(f'Você ainda tem {idade} anos, e falta {saldo} anos para se alistar')
    ano = atual + saldo # em que data foi o alistamento
    print(f'Seu Alistamento Sera em {ano} anos')
elif idade > 18: #quem ja passou dos 18
    saldo = idade - 18 # calculo da data 
    print(f'Você ja tem {idade} anos, e deveria se alista Há {saldo} anos')
    ano = atual - saldo # em que data foi o alistamento
    print(f'Seu Alistamento Foi em {ano}')