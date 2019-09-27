'''
A graph with vertices (a,b,c,d,e,f) and with all nodes interconnected(the edges)
and node a being the root.
An edge can be thought of as a node and connected neighbour(s) pair
'''
letters = {'a':['b','c'],
         'b':['d','e','f'],
         'c':['d','e','f'],
         'd':['e'],
         'e':['f','c'],
         'f':['e']
         }

class Graph():
    def __init__(self, graph=None):
        '''initialize an empty dict for the graph object'''
        if graph == None:
            graph = {}
        self.__graph = graph

    def vertices(self) -> list:
        '''
        returns a list of vertices of a graph
        '''
        return list(self.__graph.keys())

    def edges(self) -> list:
        '''
        Returns: A list of edges of the graph.
        '''
        edges: list = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                edges.append((node, neighbour))
        return edges

    def add_vertex(self, vertex) -> None:
        '''
        Add a new vertex/node to a graph
        '''
        if vertex not in self.__graph:
            self.__graph[vertex] = []

    def add_edge(self, edge) -> None:
        '''
        Add a new non-deplicate edge to a graph vertex(ices)
        '''
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        if vertex1 in self.__graph:
            self.__graph[vertex1].append(vertex2)
        else:
            self.__graph[vertex1] = [vertex2]

    def get_edges(self) -> list:
        '''
        Generate edges from an input graph
        '''
        edges = []
        for vertex in self.__graph:
            for neighbour in self.__graph[vertex]:
                if {neighbour,vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def isolated_nodes(self) -> list:
        '''
        Returns a list of isolated nodes in a graph
        '''
        isolated: list = []
        for node in self.__graph:
            if not self.__graph[node]:
                isolated += node
        return isolated


if __name__=='__main__':
    pass
    #print(edges(letters))
    #print(isolated_nodes(letters))