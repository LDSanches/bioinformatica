"""
Exercício 4 - Criando uma classe

Crie uma classe OrganismoFasta que tenha os atributos (receba eles no construtor) id, nome e sequencia.

Ela também deve ter um método calcular_tamanho_da_sequencia, que calcula o tamanho de sua própria
sequencia (ou seja, a partir do próprio atributo, esse método não necessita receber outro parametro além do self.

Dica: Se inspirar no exercício 4 da última aula!
"""

class OrganimoFasta:
    def __init__(self, id, nome, sequencia):
      self.id = id
      self.nome = nome
      self.sequencia = sequencia

    def calcular_tamanho_da_sequencia(self):
      return len(self.sequencia)


'''
# Teste igual ao test_exercicios.py:

organismo_fasta = OrganimoFasta("NC_074786.1", "Guereza hepacivirus", "ATCGATT")
print(organismo_fasta.id)
print(organismo_fasta.nome)
print(organismo_fasta.sequencia)
print(organismo_fasta.calcular_tamanho_da_sequencia())

#assert organismo_fasta.id == "NC_074786.1"
#assert organismo_fasta.nome == "Guereza hepacivirus"
#assert organismo_fasta.sequencia == "ATCGATT"

#assert organismo_fasta.calcular_tamanho_da_sequencia() == 7
'''
