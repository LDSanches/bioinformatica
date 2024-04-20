lista_completa = [*map(int,input("Digite a sua lista (separando os números por vírgula): ").split(","))]
lista_impares = []

for c in lista_completa:
  if c % 2 != 0:
    lista_impares.append(c)
    
print(f'Os números ímpares são {lista_impares}')
