from sage.graphs.graph import Graph
from collections import Counter
from itertools import combinations
from igraph import Graph as iGraph
from itertools import chain, combinations
    
class Graphix(Graph):
    def __init__(self):
        super().__init__()
        self.verticesx = {}

    def add_vertex(self, vertex):
        self.verticesx[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.verticesx:
            self.verticesx[vertex1].append(vertex2)
            self.verticesx[vertex2].append(vertex1)
        else:
            print("One or both vertices do not exist in the graph.")

    def degree(self, vertex):
        if vertex in self.verticesx:
            return len(self.verticesx[vertex])
        else:
            print("Vertex does not exist in the graph.")

    def edges(self):
        edge_list = []
        for vertex, neighbors in self.verticesx.items():
            for neighbor in neighbors:
                if (neighbor, vertex) not in edge_list and (vertex, neighbor) not in edge_list:
                    edge_list.append((vertex, neighbor))
        return edge_list

def Boolean_sum(graphs):
        # Vérification si les graphes ont le même ensemble de sommets
        vertex_set = set(graphs[0].vertices())
        for graph in graphs[1:]:
            if set(graph.vertices()) != vertex_set:
                print(set(graph.vertices()), vertex_set)
                print("The graphs do not have the same vertex set.")

        # Création du graphe résultat
        result_graph = Graph()

        # Ajout des sommets au graphe résultat
        for vertex in vertex_set:
            result_graph.add_vertex(vertex)

        # Parcours de chaque sommet
        for vertex in vertex_set:
            # Compteur du nombre d'occurrences d'une arête
            edges = []
            # Parcours de chaque graphe
            for graph in graphs:
                if vertex in graph.vertices():
                    for neighbor in graph.neighbors(vertex):
                        edges.append((min(vertex, neighbor), max(vertex, neighbor)))

            edges_count = Counter(edges)
            for edge, count in edges_count.items():
                if count % 2 != 0:
                    result_graph.add_edge(edge[0], edge[1])

        return result_graph

#The following function returns the list of all graphs of order n up to isomorphism.
def Graphs(n):
    all_graphs = []
    for s in range((n*(n-1))//2 + 1):  #Loop over all possible edge counts
        for G in graphs(n, size=s):
            all_graphs.append(G)
    return all_graphs

#The following function returns the power set except the empty set and singletons.
def power_set(list0):
    list0=list(chain(*[combinations(list0, i) for i in range(1, len(list0) + 1)]))
    list1=[]
    for u in list0:
        if len(u)>=2:
            list1.append(u)
    return list1

#The following function returns the list of all clique graphs of a set "vertexset" of vertices.
def Graphs_Clique(vertexset):
    grcliq=[]
    PS=power_set(vertexset)
    for gph in PS:
        G = Graph()
        G.add_vertices(vertexset)
        G.add_clique(gph)
        grcliq.append(G)
    return grcliq

#The following function returns non-prime graphs of order n.
def Decomposable_Graphs(n):
    NonPrime=[]
    for G in Graphs(n):
        if not G.is_prime():
            NonPrime.append(G)
    return(NonPrime)

#The following function removes the complement (or the isomorph of the complement) of each graph in the list of non-prime graphs of order n.
#def final_list(n):
#    lii=Decomposable_Graphs(n)
#    k=[]
#    for G in lii:
#        for H in lii:
#            if H.is_isomorphic(G.complement()):
#                lii.remove(H)
#                k.append(H)
#    return k

# Modify the function to include graphs of order n (7 in this case)
def final_list(n):
    lii = Decomposable_Graphs(n)
    k = []
    for G in lii:
        for H in lii:
            if H.is_isomorphic(G.complement()):
                lii.remove(H)
                k.append(H)
    return k



#The following function does the Boolean sum of a graph G and n columns of a list of graphs.
def sumF(G,lista,n):
    lis=list(chain(*[combinations(lista, i) for i in range(n, n+1)])) 
    dim=0
    for elt in lis: 
        s=G 
        for e in elt:
            s=Boolean_sum([s,e])
        if s.is_prime():
            dim=n
            return dim
    return dim


def dimension(G):
    graphclicklist=Graphs_Clique(G.vertices())
    dime=0
    for i in range(1,4):
        dime=sumF(G,graphclicklist,i)
        if dime!=0:
            return dime 
    return dime

#for G in final_list(6):
#    print("dim=", dimension(G))

# Update the loop to iterate through final_list(7)
for G in final_list(7):
    print("dim =", dimension(G))