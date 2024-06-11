lista_de_produtos = [
  { "nome": "Leite",     "quantidade": 1, "preço": 7 },
  { "nome": "Pao",       "quantidade": 6, "preço": 3 },
  { "nome": "Banana",    "quantidade": 2, "preço": 1.50 },
  { "nome": "Chocolate", "quantidade": 3, "preço": 4.50 }
]

def calcular_valor_da_compra(lista_de_produtos):
    valor_total = 0
    for produto in lista_de_produtos:
        preco_por_produto = produto["quantidade"] * produto["preço"]
        print(f"{produto['nome']} x {produto['quantidade']} = R${preco_por_produto:.2f}")
        valor_total += preco_por_produto
    print(f"Total da compra: R${valor_total:.2f}")


calcular_valor_da_compra(lista_de_produtos)