print ("Para descobrir se essa variante é relevante digite as seguintes informações")

frequencia_pop = float(input("Digite a frequencia populacional (em porcentagem):"))
gene_da_variante = str(input("Digite o gene:"))
impacto_variante = str(input("Digite a Impacto (ALTO ou BAIXO):"))
reads_variante= int(input("Digite os reads:"))
frequencia_var= float(input("Digite a frequencia alélica (em porcentagem):"))

artefato = reads_variante <10 or frequencia_var < 20
condicao1= not artefato and impacto_variante == "ALTO"
condicao2 = not artefato and (frequencia_pop < 5 and (gene_da_variante == "HFE" or gene_da_variante == "GJB2" or gene_da_variante == "MEFV"))

if condicao1 or condicao2:
    print (" Resposta: É relevante")
else:
    print ("Resposta: Não é relevante")
