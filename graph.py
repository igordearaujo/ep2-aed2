import pandas as pd
import numpy as np

# Cenário 3

# 'https://www.programiz.com/dsa/graph-adjacency-list'
class NoAdjacencia:
    def __init__(self, value):
        self.vertice = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    def add_edge(self, s, d):
        node = NoAdjacencia(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = NoAdjacencia(s)
        node.next = self.graph[d]
        self.graph[d] = node

    #Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertice " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertice), end="")
                temp = temp.next
            print(" \n")
            print()


def read_file():
    data = pd.read_csv(r'cenario3.txt', sep=" ", header=None, skiprows=2)
    data.columns=['A', 'B']
    return data

def build_graph(data):
    # Escolher entre (matriz, lista de adjacencia ou lista de pares).
    numero_vertices_max = data["A"].max()
    numero_vertices = data["A"].shape[0]
    
    arrayVertices1 = data["A"].to_list()
    arrayVertices2 = data["B"].to_list()


    grafo = Graph(int(numero_vertices_max))

    for item in range(numero_vertices - 1):
        grafo.add_edge(arrayVertices1[item], arrayVertices2[item])
    
    return grafo

def count_edges(graph):
    total_edges = 0
    i = 0

    for item in graph.graph:
        if item:
            total_edges += count_node_degree(graph, i)
        i += 1

    total_unique_edges = total_edges // 2

    return total_unique_edges + 1

def count_node_degree(graph, vertex):
    #quantas pessoas encontram 0 pessoas, quantas encontram 1 pessoa ...
    grau = 0

    vertice = graph.graph[vertex]

    while vertice:
        grau += 1
        if vertice.next:
            vertice = vertice.next
        else:
            break

    return grau

def main():
    data = read_file()
    grafo = build_graph(data)
    num_arestas = count_edges(grafo)

    qtd_encontros = [0] * 86319
    count_zero = 0
    count_zero_cinco = 0
    count_cinco_dez = 0
    count_mais_dez = 0


    for item in range(len(grafo.graph)):
        grau_vertice = count_node_degree(grafo, item)

        if grau_vertice == 0:
            count_zero += 1
        elif grau_vertice > 0 and grau_vertice <= 5:
            count_zero_cinco += 1
        elif grau_vertice > 5 and grau_vertice <= 10:
            count_cinco_dez += 1
        else:
            count_mais_dez += 1

    print(count_zero)

main()

