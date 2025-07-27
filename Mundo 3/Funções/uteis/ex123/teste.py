"""
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 119, 120, 121 e 122 para o primeiro pacote e mantenha tudo funcionando.
"""
import utilidadescev
import utilidadescev.moeda
p = float(input('Digite um preço R$'))
utilidadescev.moeda.resumo(p, 15, 10)
