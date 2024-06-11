# Exercicio 1
class AnimalDeEstimacao:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

animal = AnimalDeEstimacao("Cheetos",8)

#print(AnimalDeEstimacao)


# Exercicio 2
class Cachorro(AnimalDeEstimacao):

    def falar(self):
        print("Au Au")

class Gato(AnimalDeEstimacao):

    def falar(self):
        print("Miau")
