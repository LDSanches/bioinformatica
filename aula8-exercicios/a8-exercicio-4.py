'''
Exercício 4 -
Matéria a ser revisada: Programação Orientada a Objetos / Classes
Faça uma classe ProdutoComprado, que tem os atributos nome, quantidade, e preco.

Essa classe vai ter um método calcular_preco_total, que vai retornar o preço total do produto.
'''

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def calcular_preco_total(self):
        return self.preco * self.quantidade


produto = Produto("Leite", 2, 8)
print(produto.calcular_preco_total())
