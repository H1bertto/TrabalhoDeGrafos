from Grafo import Grafo

if __name__ == "__main__":
    print('Testes')

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

    print('\nQuestão 1')
    # Deve Retornar True
    print(Grafo().is_adjacente(1, 2, grafo_1))
    # Deve Retornar False
    print(Grafo().is_adjacente(1, 2, grafo_2))

    print('\nQuestão 2')
    # Deve Retornar 5
    print(Grafo().get_grau(grafo_1[3]))
    # Deve Retornar 2
    print(Grafo().get_grau(grafo_2[3]))

    print('\nQuestão 3')
    # Deve Retornar True
    print(Grafo().is_regular(grafo_1))
    # Deve Retornar False
    print(Grafo().is_regular(grafo_2))

    print('\nQuestão 4')
    # Deve Retornar False
    print(Grafo().is_isolado(grafo_1[4]))
    # Deve Retornar True
    print(Grafo().is_isolado(grafo_2[4]))

    print('\nQuestão 5')
    # Deve Retornar False
    print(Grafo().is_pendente(grafo_1[3]))
    # Deve Retornar True
    print(Grafo().is_pendente(grafo_2[3]))

    print('\nQuestão 6')
    # Deve Retornar False
    print(Grafo().is_nulo(grafo_1))
    # Deve Retornar True
    print(Grafo().is_nulo(grafo_3))

    print('\nQuestão 7')
    # Deve Retornar True
    print(Grafo().is_completo(grafo_1))
    # Deve Retornar False
    print(Grafo().is_completo(grafo_2))

    print('\nQuestão 8')
    # Deve Retornar True
    print(Grafo().is_conexo(grafo_1))
    # Deve Retornar False
    print(Grafo().is_conexo(grafo_2))

    print('\nQuestão 9')
    # Deve Retornar False
    print(Grafo().is_bipartido(grafo_1))
    # Deve Retornar True
    print(Grafo().is_bipartido(grafo_4))

    print('\nQuestão 10')
    # Deve Retornar grafo Nulo
    print(Grafo().get_complementar(grafo_1))
    # Deve Retornar grafo Complementar
    print(Grafo().get_complementar(grafo_5))

    print('\nQuestão 11')
    # Deve Retornar False
    print(Grafo().is_euleriano(grafo_1))
    # Deve Retornar True
    print(Grafo().is_euleriano(grafo_4))

    print('\nQuestão 13')
    # Deve Retornar False
    print(Grafo().is_unicursal(grafo_4))
    # Deve Retornar True
    print(Grafo().is_unicursal(grafo_5))

    print('\nQuestão 13')
    # Deve Retornar True
    print(Grafo().has_ciclo(grafo_2))
    # Deve Retornar False
    print(Grafo().has_ciclo(grafo_5))