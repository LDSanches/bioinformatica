# Exercicio 7 Analisador de Variantes Genéticas.
# Você está analisando uma variante genética e precisa saber se ela é relevante para análise ou não.

# Obs: Esse exercício é uma simplificação! Depois vocês vão saber avaliar de verdade!
# Você vai receber 4 parametros:
# Frequência Populacional: Frequencia da variante na população em porcentagem.
# Gene: Gene da variante.
# Impacto: Se ela está numa posição de impacto ALTO ou BAIXO.
# Reads: Quantidade de reads da variante.
# Vaf: Frequencia alélica da variante.

# A primeira coisa é tomar cuidado com a qualidade da leitura. 
#   Se a variante tiver menos de 10 reads OU uma frequência alélica abaixo de 20% 
#   a gente vai dizer que ela não é relevante, pois deve ser um artefato.

# Se ela não for um artefato temos que avaliar as seguintes coisas:
#   1) Ela só vai ser relevante se o impacto for ALTO. 
#   2) Ela não vai ser relevante se a frequência dela for menor que 5%, 
#      a não ser que esteja nos seguintes genes de exceção: 'HFE', 'MEFV' ou 'GJB2'.

v_freq_populacional = float(input('Frequencia da variante na populacao em %: '))
v_gene = input('Qual o gene? ')
v_impacto = str(input('Qual é o impacto ALTO / BAIXO? '))
v_reads = float(input('Qual de reads da variante? '))
v_vaf = float(input('Frequencia aletica da variante: '))

v_reads_limit = float(10)
v_vaf_limits = float(20)

v_artefato = (v_reads < v_reads_limit) or (v_vaf < v_vaf_limits)
v_impacto_baixo = v_impacto == 'BAIXO'
v_gene_excacao = (v_gene == HPE) or (v_gene == 'MEFV') or (v_gene == 'GJB2')
v_freq_populacional_alta = v_freq_populacional > 5

if v_artefato:
    print('Dado não é relevante, pois deve ser um artefato')
elif v_impacto_baixo or (v_freq_populacional_alta and not v_gene_excacao):
    print('Ela não é relevante')
else:
    print('É relevante')

