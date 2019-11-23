from string import digits as nums
from random import randint


class Grafo:
    def __init__(self, quant_vertices=8):
        self.vertices = list(nums)[:quant_vertices]
        print(self.vertices)
        self.generate_grafo(self.vertices)

    def generate_grafo(self, vertices):
        graph = {}
        pode_ciclo = randint(0, 1)
        print(pode_ciclo)
        for v in vertices:
            grau = randint(0, int(max(vertices)))
            if not v in graph:
                graph[v] = []
            for add in range(grau):
                num = randint(0, int(max(vertices)))
                if num not in graph[v] and (num != int(v) or pode_ciclo):
                    graph[v].append(num)
                    if not str(num) in graph:
                        graph[str(num)] = []
                    if num not in graph[v]:
                        graph[str(num)].append(int(v))
            for vtc in graph:
                if v != vtc and int(vtc) in graph[v] and int(v) not in graph[vtc]:
                    graph[vtc].append(int(v))
        graph = dict(sorted(graph.items(), key=lambda kv: kv[0]))
        print(graph)

    # Questão 1
    def is_adjacente(self):
        pass

    # Questão 2
    def get_grau(self, vertice1, vertice2):
        pass

    # Questão 3
    def is_regular(self):
        pass

    # Questão 4
    def is_isolado(self):
        pass

    # Questão 5
    def is_pendente(self):
        pass

    # Questão 6
    def is_nulo(self):
        pass

    # Questão 7
    def is_completo(self):
        pass

    # Questão 8
    def is_conexo(self):
        pass

    # Questão 9
    def is_bipartido(self):
        pass

    # Questão 10
    def get_complementar(self):
        pass

    # Questão 11
    def is_euleriano(self):
        pass

    # Questão 12
    def is_unicursal(self):
        pass

    # Questão 13
    def has_ciclo(self):
        pass

    # Questão 14
    def get_grau_de_entrada(self):
        pass

    # Questão 15
    def ordenacao_topologica(self):
        pass

    # Questão 16
    def get_transposto(self):
        pass

    # Questão 17
    def is_fortemente_conexo(self):
        pass


if __name__ == "__main__":
    Grafo()
