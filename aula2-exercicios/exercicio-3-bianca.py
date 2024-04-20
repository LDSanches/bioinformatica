cromossomo = input("Digite o cromossomo da variante (ex: chr17): ")
posicao = int(input ("Digite a posição da variante: "))
genoma_referencia = input("Digite o genoma de referência da variante (hg19 ou hg38): ")

if cromossomo == "chr17":
    if genoma_referencia == "hg19" and 41196312 <= posicao <= 41277500:
        print ("Resposta:\nSim")
    elif genoma_referencia == "hg38" and 43044295 <= posicao <= 43125483:
        print("Resposta:\nSim")
else:
    print("Resposta:\nNão")
