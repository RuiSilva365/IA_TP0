# IA_TP0
Preciso de um texto para a implementação do nosso grafo, como podes ver pelo código existe um ficheiro graph.py que é onde se escreve o formato do grafo, e o formato é assim:
#graph definition
def get_graph():
    return {
        'A': {'B': 5, 'F': 3},
        'B': {'A': 5, 'C': 2, 'G': 3},
        'C': {'B': 2, 'D': 6, 'H': 10},
        'D': {'C': 6, 'E': 3},
        'E': {'D': 3, 'F': 8, 'H': 5},
        'F': {'E': 8, 'G': 7, 'A':3},
        'G': { 'B': 3, 'F': 7, 'H': 2},
        'H': { 'C': 10, 'E': 5, 'G': 2}
    }


graph = get_graph()
print(graph)

Como podes ver, não foi feito a partir de coordenads( o que secalhar até seria mais aconselhado pelas heuristicas) contudo como o grafo era pequeno, acho que nesta fase inicial da cadeira nao vale a pena.
De qualquer das formas a inserção/leitura dos dados do grafo é nesse formato, e depois 
temos o ficheiro draw.py que desenha o grafo com a ajuda da função def get_fixed_positions():
    return {
        'A': (1, 3), 'B': (0, 2), 'C': (0, 1), 'D': (1, 0),
        'E': (2, 0), 'F': (3, 1), 'G': (3, 2), 'H': (2, 3)
    }
que ajusta o posicionamento de cada nodo para ficar semelhante ao pedido pelo professor.