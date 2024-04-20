# Exercício 2 - Calculando o RPK de Organismos
# rpk = reads_organismo / (tamanho_do_genoma_do_organismo * 1000)

organismos = [
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

for calculo_rpk in organismos:
    calculo_rpk["rpk"] = calculo_rpk["reads"] / (calculo_rpk["tamanho_genoma"] * 1000)
    print(calculo_rpk["rpk"])

print(organismos)
