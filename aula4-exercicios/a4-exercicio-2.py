# Exercício 2 - Calculando o RPK de Organismos
# rpk = reads_organismo / (tamanho_do_genoma_do_organismo * 1000)

dicionario_organismos = [
    {
        "nome": "Human immunodeficiency virus 1",
        "reads": 1000000,
        "tamanho_genoma": 8955,
    },
    {
        "nome": "Acinetobacter sp. NIPH 1865",
        "reads": 100000,
        "tamanho_genoma": 4006699,
    },
    {
        "nome": "Fungia sp.",
        "reads": 50000,
        "tamanho_genoma": 50001111,
    },

]

for novo_organismo in dicionario_organismos:
    novo_organismo["rpk"] = novo_organismo["reads"] / (novo_organismo["tamanho_genoma"] * 1000)
    print(novo_organismo["rpk"])

print(dicionario_organismos)
