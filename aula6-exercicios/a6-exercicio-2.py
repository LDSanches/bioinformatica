"""
Exercício 2 - Criando um dicionário

Escreva uma função com o nome `criar_organismo` que recebe 3 argumentos: id, nome, tamanho_do_genoma e retorna um
dicionário contendo esses três campos (com as chaves "id", "nome" e "tamanho_do_genoma").

Exemplo de uso:
>>> print(criar_organismo(10, 'HIV', 1000))
>>> {"id": 10, "nome": "HIV", 1000}
"""

def criar_organismo(id, nome, tamanho):
    dicionario = {
        'id': id, 
        'nome': nome,
        'tamanho_do_genoma': tamanho,
    }
    return dicionario

#print(criar_organismo(10, 'HIV', 1000))
