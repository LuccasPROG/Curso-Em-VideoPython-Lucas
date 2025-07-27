#crie um script que analize se o ano e um ano bissexto ou não com ifs


import datetime # datas 
ano = int(input('Que ano Deseja Analizar? Coloque 0 Para Analizar o Ano Atual:')) #Pergunta Qual ano deseja ver se é bixesto e o 0 verifica o ano atual !
if ano == 0:
    ano = datetime.date.today().year # verifica seu ano atual e coloca caso aperte 0
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  #verifica se o Ano é Bissexto !
    print(f'O Ano {ano} é um ano Bissexto!')
else:
    print(f'O Ano {ano} não é um ano Bissexto!')