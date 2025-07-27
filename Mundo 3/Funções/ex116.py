"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)

Adicione tambeem as docstrings da função
"""

def notas(*n, sit=False):
    """
    -> Função para analize de notas de varios alunos
     n -> introduz varias notas !
     sit -> caso queira (Opcional) que aparece a mensagem de se foi bom ou ruim o estado da nota atual
     return -> retorna o dicionario resultados !
    """
    resultados = dict()
    media = 0
    resultados['total'] = len(n)
    resultados['Maior'] = max(n)
    resultados['Menor'] = min(n)
    resultados['Media'] = sum(n) / len(n)
    if sit == True:
        if resultados['Media'] < 5.9:
            resultados['situação'] = 'Ruim'
        elif resultados['Media'] <= 7.9:
            resultados['situação'] = 'Razoavel'
        else:
            resultados['situação'] = 'Otima'
    return(resultados)
#inicio:
resp = notas(6.5,7,10,sit=True)
print(resp)
help(notas)