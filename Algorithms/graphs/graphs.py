'''
A graph with vertices (a,b,c,d,e,f) and with all nodes interconnected(the edges)
and node a being the root.
An edge can be thought of as a node and connected neighbour(s) pair
'''
letters = {'a':['b', 'c'],
           'b':['d', 'e'],
           'c':['d', 'e', 'f'],
           'd':['e'],
           'e':['f', 'c'],
           'f':[]
           }

class Graph(object):
    def __init__(self, graph=None):
        '''
        Initializes an empty dict for the graph object if none is given
        '''
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
        Returns a list of edges from an input graph
        '''
        edges: list = []
        for vertex in self.__graph:
            for neighbour in self.__graph[vertex]:
                if {neighbour,vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def add_vertex(self, vertex:str) -> None:
        '''
        Add a new vertex/node to a graph
        '''
        if vertex not in self.__graph:
            self.__graph[vertex] = []

    def add_edge(self, edge:str) -> None:
        '''
        Add a new non-duplicate edge to a graph vertex/vertices
        '''
        edge: set = set(edge)
        vertex1, vertex2 = tuple(edge)
        if vertex1 in self.__graph:
            self.__graph[vertex1].append(vertex2)
        else:
            self.__graph[vertex1] = [vertex2]

    def isolated_nodes(self) -> list:
        '''
        Returns a list of isolated nodes in a graph
        '''
        isolated: list = []
        for vertex in self.__graph:
            if not self.__graph[vertex]:
                isolated += [vertex]
        return isolated

    def find_path(self, start: str, end: str, path: list=None) -> list:
        '''
        Returns the path in the graph from start and end vertices
        '''
        if start not in self.__graph:
            return None
        elif path is None:
            path: list = []
        path += [start]
        if start == end:
            return path
        for vertex in self.__graph[start]:
            if vertex not in path:
                new_path = self.find_path(vertex, end, path)
                if new_path:
                    return new_path
        return None

    def vertex_degree(self, vertex: str) -> int:
        '''
        Calculates the degree of a vertex. The degree of a vertex
        is the number of edges connecting it i.e. the number of adjacent
        vertices.
        '''
        adjacent = self.__graph(vertex)
        degree = len(adjacent) + adjacent.count(vertex)
        return degree

    



if __name__ == '__main__':
    graph = Graph(letters)
    print(graph.edges())
    print(graph.find_path('a', 'f'))