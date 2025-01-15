class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"{self.nome} - {self.nota}"
    
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2].nota
    menores = [estudante for estudante in lista if estudante.nota < pivo]
    iguais = [estudante for estudante in lista if estudante.nota == pivo]
    maiores = [estudante for estudante in lista if estudante.nota > pivo]
    return quicksort(maiores) + iguais + quicksort(menores)

estudantes = [
    Estudante("Heitor", 9.5),
    Estudante("João", 7.0),
    Estudante("Maria", 8.0),
    Estudante("Letícia", 6.5),
    Estudante("Pedro", 7.5),
    Estudante("Poliana", 6.5)
]

estudantes_ordenados = quicksort(estudantes)

print("Estudantes ordenados por nota:")
for estudante in estudantes_ordenados:
    print(estudante)
