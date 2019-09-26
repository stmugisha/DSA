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

def edges(graph: dict) -> list:
    '''
    Generates all edges from a given graph.
    Args: a graph of type dict.
    Returns: A list of edges.
    '''
    edges: list = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

def isolated_nodes(graph: dict) -> list:
    '''
    Returns a list of isolated nodes in a graph
    '''
    isolated: list = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated


if __name__=='__main__':
    print(edges(letters))
    print(isolated_nodes(letters))