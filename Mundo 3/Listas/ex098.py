estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa :'))
    estado['Sigla'] = str(input('Sigla  Do Estado:'))
    brasil.append(estado.copy()) # copy faz uma copia igual [:] na lista 
for s in brasil:
    for  i, v in s.items():
        print(f'O Campo {i} Tem valor {v}')
#+================================================================+

'''dados = {'nome' : 'Lucas', 'Idade' : '18', 'Sexo' : 'Masculino'
}
dados['peso'] = '119kg'
del dados['Idade']
for i, v in dados.items():
    print(f'{i} = {v}')'''


#==========================================================================

'''print(dados.keys()) # Mostra so  as 'Variaves' 
print(dados.values()) # Mostra so Os nomes dentro da variavel
print(dados.items()) # mostra tudo tanto nome e quanto variavel'''