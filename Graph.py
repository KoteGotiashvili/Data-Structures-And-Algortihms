# https://python-course.eu/applications-python/graphs-python.php
# Everything is on this link

# C is middle node and connects to all, f is alone
import networkx as nx
import matplotlib.pyplot as plt
#find edges between graphs
class Graph:
    def __init__(self, graph_dict = None):
        if not graph_dict:
            graph_dict=None
        self._graph_dict = graph_dict
    def edges(self, vertice):
        """ Returns all edges of a vertices in a list """
        return self._graph_dict[vertice]
    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return self._graph_dict.keys()
    # visualized graoh
    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """


    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """


    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """


    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj

    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    # def visualize_graph(graph):
    #     G = nx.Graph()
    #     for node in graph:
    #        G.add_node(node)  # Fixed typo: add_node instead of add_nodes_from
    #         for neighbor in graph[node]:
    #             G.add_edge(node, neighbor)  # Fixed typo: add_edge instead of add_edges_from
    #     nx.draw(G, with_labels=True)
    #     plt.show()

g = { "a" : {"c"},
          "b" : {"c", "e", "a", "d", "f"},
          "c" : {"a", "b", "d", "e"},
          "d" : {"c"},
          "e" : {"c", "b"},
          "f" : {}
        }
graph = Graph(g)

for vertice in graph.all_vertices():
    print(f"Edges of vertice {vertice}: ", graph.edges(vertice))