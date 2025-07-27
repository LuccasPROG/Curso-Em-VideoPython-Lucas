#FINAL, CRIE UM SCIPRT QUE DE PARA CADASTRA PESSOA, VER NOVA PESSOA E SAIR DO SISTEMA QUE FIQUE 
#SALVA NO CADASTRO PARA SEMPRE USANDO TUDO OQUE VOCÊ APRENDEU ATE AQUI
from lib.interface import *
from lib.arquivo import * # * importa tudo !
from time import sleep

arq = 'cadastro.txt'
if not ArquivoExiste(arq):
   criararquivo(arq)
while True:
   resposta = menu(['Ver pessoas cadastradas', 'Cadastra nova pessoa', 'Sair do sistema'])
   if resposta == 1:
      #opção de listar o conteudo de um arquivo!
      lerArquivo(arq)
   elif resposta == 2:
      cabeçalho('NOVO CADASTRO')
      nome = str(input('Digite o Nome:'))
      idade = leiaint('Idade:')
      cadastra(arq, nome, idade)
   elif resposta == 3:
      cabeçalho('Saindo do Sistema . . . Até Logo!')
      break
   else:
      print('\033[31mErro: Numero não Existente!\033[m')
   sleep(2)
