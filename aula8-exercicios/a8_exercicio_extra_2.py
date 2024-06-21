"""
Exercício 2 - Identificacação do início de um Open Read Frame

Dada uma sequência começada com qualquer base e terminada com algum codon de parada ('TAA', 'TAG' ou 'TGA'),
faça uma função que ache o início dela e retorne a sequencia.

Exemplo:

"TATACCTATGCCCGGGTAA" -> "ATGCCCGGGTAA".

Explicação: A sequencia começa com TAT..., o que não faz ela ser codificada.
Então, percorri a sequencia até achar o ATG (ponto de início) e peguei o resto dela (não me preocupei com o fim,
porque o enunciado já diz que ela termina corretamente num codon de parada.

Dica: Qualquer coisa reveja o exercício da aula.

Note que diferentemente do outro não há a necessidade de percorrer de 3 em 3 sempre,
afinal antes de começar a leitura de fato, a procura pode ser feita de um em um.
"""

def achar_orf_a_partir_do_inicio(sequencia):
    orf = ""
    orf_inicio = 'ATG'
    index_inicio = sequencia.find(orf_inicio)
    
    if index_inicio != -1:
        return sequencia[index_inicio:]
    else:
        return None  # Retorna None se não encontrar o códon de início

'''
# Teste igual ao test_exercicios.py:
orf = achar_orf_a_partir_do_inicio("TATACCTATGCCCGGGTAA")
print(orf)
#assert orf == "ATGCCCGGGTAA"

orf = achar_orf_a_partir_do_inicio("CTACGTACCTATGCAAATGCCATAA")
print(orf)
#assert orf == "ATGCAAATGCCATAA"
'''