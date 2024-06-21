"""
Exercício Exemplo - Achar maior valor:

Esse é um exercício de exemplo.

Crie uma função que recebe uma lista e retorna o maior valor dessa lista.

A função deve se chamar necessariamente `achar_maior_valor`, por ela vai ser importada para teste usando esse nome.

Ex:
>>> print(achar_maior_valor([1, 10, 11]))
>>> 11
"""

# Exemplo de resolução:
def achar_maior_valor(lista):
    maior_valor = 0
    for i in range(len(lista)):
        if i == 0:
            maior_valor = lista[i]
        elif lista[i] > maior_valor:
            maior_valor = lista[i]
    return maior_valor

#print(achar_maior_valor([1, 10, 11]))
#print(achar_maior_valor([-1, -100, -111]))

"""
Obs: Para esse exercício não é necessário chamar a função `achar_maior_valor` nesse arquivo, 
porque o arquivo de testes irá importar sua funcao e testar ela, por exemplo:

def test_ex_0():
    import exercicio_0_exemplo
    
    assert exercicio_0_exemplo.achar_maior_valor([1, 88, 0]) == 88
    assert exercicio_0_exemplo.achar_maior_valor([-1, -10, -100]) == -1
    
Porém para você validar se sua funcao esta funcionando local, recomendo que você chame sua funcão algumas vezes:

Ex:
print(achar_maior_valor([1, 10, 11]))
print(achar_maior_valor([-1, -100, -111]))

Etc..
"""