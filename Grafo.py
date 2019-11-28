class Grafo:
    def __init__(self, grafo=None, direcionado=False):
        if grafo is not None and not direcionado:
            nulo = self.is_nulo(grafo)
            if not nulo[0]:
                print(self.is_adjacente(1, 2, grafo))
                print(self.get_grau(grafo[3]))
                print(self.is_regular(grafo))
                print(self.is_isolado(grafo[4]))
                print(self.is_pendente(grafo[3]))
                print(nulo)
                print(self.is_completo(grafo))
                print(self.is_conexo(grafo))
                print(self.is_bipartido(grafo))
                print(self.get_complementar(grafo))
                print(self.is_euleriano(grafo))
                print(self.is_unicursal(grafo))
                print(self.has_ciclo(grafo))

        if grafo is not None and direcionado:
            self.get_grau_de_entrada(4, grafo)
            self.ordenacao_topologica()
            self.get_transposto(grafo)
            self.is_fortemente_conexo()

    # Para Grafos Não Direcionados ----------------------------------------------
    # Questão 1
    def is_adjacente(self, vertice1, vertice2, grafo):
        # Se o vértice 2 estiver na lista de de adjacência do vértice 1, eles serão adjacentes
        if vertice2 in grafo[vertice1]:
            return True, f'Vertice {vertice1} É Adjacente de Vertice {vertice2}'
        else:
            return False, f'Vertice {vertice1} Não é Adjacente de Vertice {vertice2}'

    # Questão 2
    def get_grau(self, vertice):
        return f'Grau do Vértice {vertice} é:', len(vertice)

    # Questão 3
    def is_regular(self, grafo):
        grau = len(list(grafo.values())[0])
        for vertice in grafo.keys():
            if len(grafo[vertice]) != grau:
                return False, 'O Grafo não é Regular'
        return True, 'O Grafo é Regular'

    # Questão 4
    def is_isolado(self, vertice):
        if len(vertice) == 0:
            return True, f'O Vértice {vertice} é Isolado'
        else:
            return False, f'O Vértice {vertice} não é Isolado'

    # Questão 5
    def is_pendente(self, vertice):
        if len(vertice) == 1:
            return True, f'O Vértice {vertice} é Pendente'
        else:
            return False, f'O Vértice {vertice} não é Pendente'

    # Questão 6
    def is_nulo(self, grafo):
        for vertice in grafo.keys():
            if len(grafo[vertice]) != 0:
                return False, 'O Grafo não é Nulo'
        return True, 'O Grafo é Nulo'

    # Questão 7
    def is_completo(self, grafo):
        if not self.is_nulo(grafo)[0]:
            for vertice1 in grafo.keys():
                for vertice2 in grafo.keys():
                    if vertice2 not in grafo[vertice1] and vertice1 != vertice2:
                        return False, 'O Grafo não é Completo'
            return True, 'O Grafo é Completo'
        return False, 'O Grafo não é Completo'

    # Questão 8
    def is_conexo(self, grafo):
        for vertice in grafo.keys():
            if self.is_isolado(grafo[vertice])[0]:
                return False, 'O Grafo não é Conexo'
        return True, 'O Grafo é Conexo'

    # Questão 9
    def is_bipartido(self, grafo):
        g1 = dict(list(grafo.items())[len(grafo)//2:])
        g2 = dict(list(grafo.items())[:len(grafo)//2])
        contem = False

        for vertice1 in g1.keys():
            if vertice1 not in g1[vertice1]:
                for vertice2 in g2.keys():
                    v2_group = list(g2.values())[0] + list(g2.values())[1] + list(g2.values())[2]
                    if vertice1 in g2[vertice2] and vertice2 not in v2_group:
                        contem = True
                        break
                if not contem:
                    return False, 'O Grafo não é Bipartido'
            else:
                return False, 'O Grafo não é Bipartido'

        for vertice2 in g2.keys():
            if vertice2 not in g2[vertice2]:
                for vertice1 in g1.keys():
                    v1_group = list(g1.values())[0] + list(g1.values())[1] + list(g1.values())[2]
                    if vertice2 in g1[vertice1] and vertice1 not in v1_group:
                        contem = True
                        break
                if not contem:
                    return False, 'O Grafo não é Bipartido'
            else:
                return False, 'O Grafo não é Bipartido'
        return True, 'O Grafo é Bipartido'

    # Questão 10
    def get_complementar(self, grafo):
        complementar = {
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
               }
        if not self.is_completo(grafo)[0]:
            for vertice1 in grafo.keys():
                for vertice2 in grafo.keys():
                    if vertice2 not in grafo[vertice1] and vertice1 != vertice2:
                        complementar[vertice1].append(vertice2)

        return 'Grafo:', grafo, 'seu Grafo Complementar é:', complementar

    # Questão 11
    def is_euleriano(self, grafo):
        if self.is_conexo(grafo)[0]:
            for vertice in grafo.keys():
                if self.get_grau(grafo[vertice])[1] % 2 != 0:
                    return False, 'O Grafo não é Euleriano'
            return True, 'O Grafo é Euleriano'
        return False, 'O Grafo  não é Euleriano'

    # Questão 12
    def is_unicursal(self, grafo):
        count_vertice_impar = 0
        for vertice in grafo.keys():
            if self.get_grau(grafo[vertice])[1] % 2 != 0:
                count_vertice_impar += 1

        if count_vertice_impar == 2:
            return True, 'O Grafo é Unicursal'
        else:
            return False, 'O Grafo não é Unicursal'

    # Questão 13
    def has_ciclo(self, grafo):
        if not self.is_nulo(grafo)[0]:
            for vertice in grafo.keys():
                if vertice in grafo[vertice]:
                    return True, 'O Grafo tem Ciclo'
        return False, 'O Grafo não tem Ciclo'

    # Para Grafos Direcionados ----------------------------------------------
    # Questão 14
    def get_grau_de_entrada(self, vertice, grafo):
        count_entrada = 0
        for v1 in grafo.keys():
            if vertice in grafo[v1]:
                count_entrada += 1
        return f'O Grau de Entrada do Vértice {vertice} é: {count_entrada}'

    # Questão 15
    def ordenacao_topologica(self):
        pass

    # Questão 16
    def get_transposto(self, grafo):
        grafo_transposto = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
    }
        for vertice1 in grafo.keys():
            for vertice2 in grafo.keys():
                if vertice2 in grafo[vertice1] and vertice1 != vertice2:
                    grafo_transposto[vertice2].append(vertice1)
        return f'Grafo: {grafo} O Grafo Transposto: {grafo_transposto}'

    # Questão 17
    def is_fortemente_conexo(self, grafo):
        for vertice1 in grafo.keys():
            for vertice2 in grafo.keys():
                if vertice1


if __name__ == "__main__":
    # Grafos Representados como uma Lista de Ajacência
    grafo_1 = {
        1: [2, 3, 4, 5, 6],
        2: [1, 3, 4, 5, 6],
        3: [1, 2, 4, 5, 6],
        4: [1, 2, 3, 5, 6],
        5: [1, 2, 3, 4, 6],
        6: [1, 2, 3, 4, 5],
    }

    grafo_2 = {
        1: [1, 5, 6],
        2: [1, 3, 6],
        3: [2],
        4: [],
        5: [1, 6],
        6: [1, 2, 5],
    }

    grafo_3 = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
    }

    grafo_4 = {
        1: [4, 5],
        2: [5, 6],
        3: [6, 4],

        4: [1, 2],
        5: [2, 3],
        6: [3, 1],
    }

    grafo_5 = {
        1: [5, 6],
        2: [4, 3, 6],
        3: [2, 4],
        4: [3, 2],
        5: [1, 6],
        6: [1, 2, 5],
    }

    grafo_direcionado_1 = {
        1: [5, 6],
        2: [4, 3, 6],
        3: [1, 4],
        4: [],
        5: [6],
        6: [3, 4],
    }
    # -------------------------------------------------

    # Inicio dos Resultados
    print('Grafo 1')
    Grafo(grafo_1)
    print('\nGrafo 2')
    Grafo(grafo_2)
    print('\nGrafo 3')
    Grafo(grafo_3)
    print('\nGrafo 4')
    Grafo(grafo_4)
    print('\nGrafo 5')
    Grafo(grafo_5)
    print('\nGrafo Direcionado 1')
    Grafo(grafo_direcionado_1, direcionado=True)
