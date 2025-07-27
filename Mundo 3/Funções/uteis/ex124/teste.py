"""
Dentro do pacote utilidadesCeV que criamos no desafio 123, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""
from utilidadescev import dados
from utilidadescev import moeda

p = dados.leiaDinheiro('Digite um Numero: R$')
moeda.resumo(p, 15, 10)
