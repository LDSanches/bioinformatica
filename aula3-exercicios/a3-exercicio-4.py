# """
# #### Exercício 4 - Lista de organismos
# 
# Você recebeu uma lista que contém, para cada organismos detectado numa amostra, uma outra lista contendo a 
# quantidade de leituras que esse organismo teve em cada identificador taxonômico.
# 
# Obs: Deixei a lista direto no exercício para facilitar. Mas faça o código para descobrir, não coloque a resposta direto!
# 
# Por exemplo:
# 
# [[100, 200, 300], [1, 99, 10000], [1, 1, 1]].
# 
# Eu quero que você identifique o organismo que teve a maior média de leituras entre todos os organismos da lista.
# 
# Ao identificar digite a posição em que esse organismo se encontra na lista.
# 
# No exemplo acima, você imprimiria:
# 
# "O organismo com maior média é o da posição 1 da lista."
# 
# Porque o organismo da posição 0 tem média de (100 + 200 + 300) / 3 = 200, o organismo da posição 0
# tem média de (1 + 99 + 10000) / 3 = 3366,66 e o da posição 2 tem média de (1 + 1 + 1) / 3 = 1.
# 
# Logo o da posição 1 é maior.
# 
# ------
# 
# Exemplo:
# lista_de_organismos = [[100, 200, 300], [1, 99, 10000], [1, 1, 1]]
# 
# Resposta:
# O organismo com maior média é o da posição 1 da lista.
# 
# Dica: Utilize mais de um for para resolver o exercício, um para a lista de organismos e um para cada lista. Cuidado com a identação.
# 
# O cálculo de média já foi feito em sala e pode ser usado de exemplo.
# """
# 
# # Lista
# lista_de_organismos = [[50, 50, 50], [125, 99, 12], [19, 91, 42], [40, 189, 0], [1, 0, 0], [100, 100, 70], [99, 12, 12]]
# 
# # Fazer a partir daqui

lista_de_organismos = [[50, 50, 50], [125, 99, 12], [19, 91, 42], [40, 189, 0], [1, 0, 0], [100, 100, 70], [99, 12, 12]]
media_lista_de_organismos = []

tamanho_lista = len(lista_de_organismos)

for i in range(tamanho_lista):
    tamanho_lista_int = len(lista_de_organismos[i])
    #print(tamanho_lista_int)

    for j in range(tamanho_lista_int):
        n_lista = lista_de_organismos[i][j]
        if j == 0:
            total_listas = lista_de_organismos[i][j]
        else:
            total_listas = total_listas + lista_de_organismos[i][j]
    media_listas = total_listas / tamanho_lista_int
    #print(total_listas)
    #print(int(media_listas))

    media_lista_de_organismos.append(int(media_listas))

print(media_lista_de_organismos)

tamanho_media_lista_de_organismos = len(media_lista_de_organismos)
maior_media_listas = 0

for k in range(tamanho_media_lista_de_organismos):
    if k == 0:
        maior_media_listas = media_lista_de_organismos[k]
    else:
        if maior_media_listas < media_lista_de_organismos[k]:
            maior_numero_lista = media_lista_de_organismos[k]
            posicao_lista = k

#print(maior_numero_lista)
#print(posicao_lista)

print(f'Resposta:\nO organismo com maior média é o da posição {posicao_lista} da lista.')



# Outra forma:
lista_de_organismos = [[50, 50, 50], [125, 99, 12], [19, 91, 42], [40, 189, 0], [1, 0, 0], [100, 100, 70], [99, 12, 12]]
maior_media = 0
posicao_do_maior_organismo = 0

for i in range(len(lista_de_organismos)):
    lista_de_medicoes = int(lista_de_organismos[i])

    soma_medicoes = 0
    for valor in lista_de_medicoes:
        soma_medicoes += valor

    media_medicoes = soma_medicoes / len(lista_de_medicoes)

    if i == 0:
        maior_media = media_medicoes
        posicao_do_maior_organismo = i
    elif media_medicoes > maior_media:
        maior_media = media_medicoes
        posicao_do_maior_organismo = i

print(f'Resposta:\nO organismo com maior média é o da posição {posicao_do_maior_organismo} da lista.')