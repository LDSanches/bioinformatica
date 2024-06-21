def test_ex_0():
    import exercicio_0_exemplo

    assert exercicio_0_exemplo.achar_maior_valor([1, 88, 0]) == 88
    assert exercicio_0_exemplo.achar_maior_valor([-1, -10, -100]) == -1


def test_ex_1():
    from exercicio_1 import calcular_area_e_perimetro_circulo

    area = round(calcular_area_e_perimetro_circulo(10)[0])
    perimetro = round(calcular_area_e_perimetro_circulo(10)[1])

    assert area == 314
    assert perimetro == 63

    area = round(calcular_area_e_perimetro_circulo(3)[0])
    perimetro = round(calcular_area_e_perimetro_circulo(3)[1])

    assert area == 28
    assert perimetro == 19


def test_ex_2():
    from exercicio_2 import achar_orf_a_partir_do_inicio

    orf = achar_orf_a_partir_do_inicio("TATACCTATGCCCGGGTAA")
    assert orf == "ATGCCCGGGTAA"

    orf = achar_orf_a_partir_do_inicio("CTACGTACCTATGCAAATGCCATAA")
    assert orf == "ATGCAAATGCCATAA"


def test_ex_3():
    from exercicio_3 import achar_organismo_com_maior_sequencia

    lista_de_organismos = [
        {"id": "NC_074786.1", "nome": "Guereza hepacivirus", "sequencia": "ATCGATT"},
        {"id": "NC_074787.1", "nome": "Hepatitis GB", "sequencia": "ATC"},
        {"id": "NC_076029.1", "nome": "Bovine viral diarrhea virus", "sequencia": "ATCATCGATTATCGATT"},
    ]
    nome = achar_organismo_com_maior_sequencia(lista_de_organismos)
    assert nome == ("Bovine viral diarrhea virus")

    lista_de_organismos = [
        {"id": "NC_074786.1", "nome": "Guereza hepacivirus", "sequencia": "ATCGATT"},
        {"id": "NC_074787.1", "nome": "Hepatitis GB", "sequencia": "ATCCCAAGAGAAGGAGCCAAA"},
    ]

    nome = achar_organismo_com_maior_sequencia(lista_de_organismos)
    assert nome == ("Hepatitis GB")


def test_ex_4():
    from exercicio_4 import OrganimoFasta
    organismo_fasta = OrganimoFasta("NC_074786.1", "Guereza hepacivirus", "ATCGATT")

    assert organismo_fasta.id == "NC_074786.1"
    assert organismo_fasta.nome == "Guereza hepacivirus"
    assert organismo_fasta.sequencia == "ATCGATT"

    assert organismo_fasta.calcular_tamanho_da_sequencia() == 7
    