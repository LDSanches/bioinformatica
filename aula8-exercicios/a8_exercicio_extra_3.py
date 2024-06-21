"""
Exercício 3 - Achando o organismos com maior frequencia.

Dada uma lista de organismos representados por um dicionário com as chaves id, nome e sequencia,
crie uma função achar_organismo_com_maior_sequencia que ache o organismo que tem a maior sequencia
e retorne o nome dele (atenção, retorne apenas o nome!).

Ex:

lista_de_organismos = [
    { "id": "NC_074786.1", "nome": "Guereza hepacivirus", "sequencia": "ATCGATT" },
    { "id": "NC_074787.1", "nome": "Hepatitis GB", "sequencia": "ATC" },
    { "id": "NC_076029.1", "nome": "Bovine viral diarrhea virus", "sequencia": "ATCATCGATTATCGATT" },
]

>>> print(achar_organismo_com_maior_sequencia(lista_de_organismos)
>>> "Bovine viral diarrhea virus"
"""

def achar_organismo_com_maior_sequencia(lista_de_organismos):
    maior_sequencia = 0
    nome_do_organismo_maior = ""

    for organismo in lista_de_organismos:
        comprimento_sequencia = len(organismo['sequencia'])
        
        if comprimento_sequencia > maior_sequencia:
            maior_sequencia = comprimento_sequencia
            nome_do_organismo_maior = organismo['nome']
    
    return nome_do_organismo_maior

'''
# Teste igual ao test_exercicios.py:
lista_de_organismos = [
    {"id": "NC_074786.1", "nome": "Guereza hepacivirus", "sequencia": "ATCGATT"},
    {"id": "NC_074787.1", "nome": "Hepatitis GB", "sequencia": "ATC"},
    {"id": "NC_076029.1", "nome": "Bovine viral diarrhea virus", "sequencia": "ATCATCGATTATCGATT"},
]
nome = achar_organismo_com_maior_sequencia(lista_de_organismos)
print(nome)
#assert nome == ("Bovine viral diarrhea virus")

lista_de_organismos = [
    {"id": "NC_074786.1", "nome": "Guereza hepacivirus", "sequencia": "ATCGATT"},
    {"id": "NC_074787.1", "nome": "Hepatitis GB", "sequencia": "ATCCCAAGAGAAGGAGCCAAA"},
]

nome = achar_organismo_com_maior_sequencia(lista_de_organismos)
print(nome)
#assert nome == ("Hepatitis GB")
'''