#!pip install biopython

from Bio import SeqIO

def imprimir_resumo_do_fasta(caminho_do_arquivo):
  for record in SeqIO.parse(caminho_do_arquivo, "fasta"):
    print(record.id)
    print("O tamanho da sequencia é", len(record.seq))
    print("O organismo é", record.description)
